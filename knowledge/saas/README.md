# SaaS Knowledge Base

Base de conocimiento de monetizacion y crecimiento SaaS para Gesterum.

## Flujo
1. Definir fuentes en `data/saas_sources.json`.
2. Ejecutar scraper.
3. Consumir `knowledge/saas/knowledge.jsonl` y `knowledge/saas/raw/`.

## Ejecucion
```sh
python3 scripts/knowledge_scraper.py \
  --sources data/saas_sources.json \
  --outdir knowledge/saas
```
