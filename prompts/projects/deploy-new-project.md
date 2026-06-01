# Prompt: deploy-new-project

Objetivo: desplegar un proyecto nuevo sin romper servicios existentes.

## Entrada minima
- repo y branch
- stack (dotnet/node/python)
- dominio/subdominio o subruta
- puerto interno
- endpoint health

## Secuencia
1) precheck de host y nginx
2) build/publish
3) config reverse proxy
4) verificacion end-to-end
5) rollback documentado

## Criterio de done
- endpoint responde 200
- logs sin errores criticos
- rollback probado o listo para ejecucion inmediata
