# Runbooks

## estudio-contable
- Validar puertos 5043/7051 libres.
- Ejecutar `start_estudio_contable.sh`.
- Verificar `curl -fsS http://127.0.0.1:5043/health`.

## marketup-sales
- Verificar `ALLOW_DEV_LOGIN=false` en prod.
- Validar `/config` y bloqueo de `/auth/dev-login`.

## notas-sqlite-bot
- Backup de `notes.db` antes de cambios de esquema.
