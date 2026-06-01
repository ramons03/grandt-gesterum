#!/usr/bin/env python3
import argparse
import json
import os
import re
import ssl
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from html import unescape
from html.parser import HTMLParser
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen


@dataclass
class Source:
    source_id: str
    topic: str
    url: str


class SimpleExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.capture_tags = {"p", "li", "h1", "h2", "h3"}
        self.skip_tags = {"script", "style", "noscript", "svg"}
        self._tag_stack = []
        self._skip_depth = 0
        self._buffer = []
        self._segments = []
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        self._tag_stack.append(tag)
        if tag in self.skip_tags:
            self._skip_depth += 1
        if tag == "title":
            self._in_title = True
        if self._skip_depth == 0 and tag in self.capture_tags:
            self._buffer.append("\n")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if self._skip_depth > 0 and tag in self.skip_tags:
            self._skip_depth -= 1
        if tag == "title":
            self._in_title = False
        if self._skip_depth == 0 and tag in self.capture_tags:
            text = "".join(self._buffer).strip()
            if text:
                self._segments.append(text)
            self._buffer = []
        if self._tag_stack:
            self._tag_stack.pop()

    def handle_data(self, data):
        text = unescape(data or "")
        if not text.strip():
            return
        if self._in_title:
            self.title += text.strip() + " "
        if self._skip_depth > 0:
            return
        if self._tag_stack and self._tag_stack[-1] in self.capture_tags:
            self._buffer.append(text)

    def get_title(self):
        return normalize_ws(self.title).strip() or "sin_titulo"

    def get_text(self):
        lines = []
        for seg in self._segments:
            s = normalize_ws(seg)
            if len(s) >= 40:
                lines.append(s)
        return "\n".join(lines)


def normalize_ws(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def safe_filename(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-") or "file"


def fetch_html(url: str, timeout: int = 25) -> str:
    req = Request(
        url,
        headers={
            "User-Agent": "grandt-gesterum-knowledge-scraper/1.0 (+https://github.com/ramons03/grandt-gesterum)",
            "Accept": "text/html,application/xhtml+xml"
        },
    )
    context = ssl.create_default_context()
    with urlopen(req, timeout=timeout, context=context) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        raw = resp.read()
        return raw.decode(charset, errors="replace")


def parse_sources(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    result = []
    for item in data.get("sources", []):
        result.append(Source(
            source_id=item["id"],
            topic=item.get("topic", "general"),
            url=item["url"]
        ))
    return result


def main():
    parser = argparse.ArgumentParser(description="Scraper de conocimiento para grandt-gesterum")
    parser.add_argument("--sources", required=True, help="Archivo JSON de fuentes")
    parser.add_argument("--outdir", required=True, help="Directorio de salida")
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    raw_dir = os.path.join(args.outdir, "raw")
    os.makedirs(raw_dir, exist_ok=True)

    sources = parse_sources(args.sources)
    if not sources:
        print("No hay fuentes configuradas", file=sys.stderr)
        return 2

    extracted_at = datetime.now(timezone.utc).isoformat()
    manifest = {
        "generated_at_utc": extracted_at,
        "total_sources": len(sources),
        "items": []
    }

    jsonl_path = os.path.join(args.outdir, "knowledge.jsonl")
    with open(jsonl_path, "w", encoding="utf-8") as out_jsonl:
        for src in sources:
            print(f"[scrape] {src.source_id} -> {src.url}")
            record = {
                "id": src.source_id,
                "topic": src.topic,
                "url": src.url,
                "status": "ok",
                "title": "",
                "text_chars": 0,
                "error": None,
                "file": None,
            }
            try:
                html = fetch_html(src.url)
                parser = SimpleExtractor()
                parser.feed(html)
                title = parser.get_title()
                text = parser.get_text()
                if not text:
                    raise RuntimeError("extraccion vacia")

                file_name = safe_filename(src.source_id) + ".md"
                file_path = os.path.join(raw_dir, file_name)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"# {title}\n\n")
                    f.write(f"- source_id: {src.source_id}\n")
                    f.write(f"- topic: {src.topic}\n")
                    f.write(f"- url: {src.url}\n")
                    f.write(f"- extracted_at_utc: {extracted_at}\n\n")
                    f.write(text + "\n")

                payload = {
                    "id": src.source_id,
                    "topic": src.topic,
                    "url": src.url,
                    "title": title,
                    "extracted_at_utc": extracted_at,
                    "text": text,
                }
                out_jsonl.write(json.dumps(payload, ensure_ascii=False) + "\n")

                record["title"] = title
                record["text_chars"] = len(text)
                record["file"] = os.path.relpath(file_path, args.outdir)
            except (HTTPError, URLError, TimeoutError, RuntimeError, Exception) as ex:
                record["status"] = "error"
                record["error"] = str(ex)

            manifest["items"].append(record)

    manifest_path = os.path.join(args.outdir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    index_path = os.path.join(args.outdir, "INDEX.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("# Knowledge Index - Accounting\n\n")
        f.write(f"Generated at (UTC): {extracted_at}\n\n")
        for item in manifest["items"]:
            status = item["status"]
            if status == "ok":
                f.write(f"- [{item['id']}]({item['file']}) | topic={item['topic']} | chars={item['text_chars']}\n")
            else:
                f.write(f"- {item['id']} | ERROR: {item['error']}\n")

    ok_count = sum(1 for x in manifest["items"] if x["status"] == "ok")
    print(f"Done. ok={ok_count}/{len(manifest['items'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
