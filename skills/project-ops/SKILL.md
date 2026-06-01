---
name: project-ops
description: Orquesta cambios operativos en los proyectos activos del workspace con metodologia Precheck->Ejecucion->Verificacion->Rollback. Usar cuando se requiera intervenir estudio-contable, marketup-sales, portal-empleado, sde-cobros, notas-sqlite-bot o fb-video-downloader con criterios de seguridad y validacion reproducible.
---

# project-ops

## Procedimiento base
1. Identificar proyecto objetivo y su prompt en `prompts/projects/`.
2. Seleccionar agente lider segun dominio en `prompts/agents/`.
3. Ejecutar secuencia obligatoria:
   - Precheck
   - Ejecucion
   - Verificacion
   - Rollback
4. Entregar comandos exactos, evidencia y riesgos.

## Referencias
- Para runbooks concretos por proyecto, leer `references/runbooks.md`.
