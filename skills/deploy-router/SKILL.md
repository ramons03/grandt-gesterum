---
name: deploy-router
description: Orquesta despliegues de nuevos proyectos usando router determinista de agentes (linux, dotnet, frontend, devops-cicd) y estandar operativo de Nginx/proxy/build/release/rollback. Usar cuando se pida deploy de cualquier app nueva o existente.
---

# deploy-router

## Procedimiento
1. Clasificar stack del proyecto (dotnet/node/python/mixto).
2. Seleccionar agente lider segun matriz en `references/agent-routing.md`.
3. Cargar runbook de despliegue en `references/deploy-runbook.md`.
4. Ejecutar secuencia obligatoria:
   - Precheck
   - Ejecucion
   - Verificacion
   - Rollback
5. Registrar evidencia y riesgos.

## Regla de liderazgo
- API .NET + frontend: lider dotnet, soporte frontend.
- build/release/deploy: lider devops-cicd.
- nginx/host: soporte obligatorio linux.

## Salida minima
- plan de deploy,
- comandos exactos,
- smoke checks,
- plan de contingencia.
