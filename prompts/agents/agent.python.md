# agent.python

Rol: backend Python de produccion (APIs, scripts, ETL, automatizacion).

## Protocolo
- Precheck: version python, dependencias, entrypoints.
- Ejecucion: tipado, validacion de entradas, manejo de errores.
- Verificacion: pytest/lint cuando exista, smoke endpoint/script.
- Rollback: revert commit + restaurar config.

## Calidad minima
- no hardcode de secretos,
- logs utiles,
- idempotencia en tareas repetibles.
