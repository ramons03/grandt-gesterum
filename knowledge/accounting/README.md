# Accounting Knowledge Base

Este directorio contiene conocimiento extraido por scraper para uso en prompts/skills.

## Flujo
1. Definir fuentes en `data/accounting_sources.json`.
2. Ejecutar scraper.
3. Consumir `knowledge/accounting/knowledge.jsonl` y archivos en `raw/`.

## Ejecucion
```sh
python3 scripts/knowledge_scraper.py \
  --sources data/accounting_sources.json \
  --outdir knowledge/accounting
```
