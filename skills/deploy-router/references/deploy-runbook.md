# Deploy Runbook (Generic)

## Precheck
- branch y estado git
- variables de entorno requeridas
- puertos libres/ocupados
- backups de config y artefactos

## Ejecucion
- build reproducible
- publish/artifact
- actualizar runtime target
- configurar/revisar vhost nginx

## Verificacion
- `nginx -t`
- reload nginx
- health endpoint local
- smoke endpoint publico
- logs de app y nginx

## Rollback
- restaurar artefacto previo
- restaurar vhost backup
- recargar nginx
- confirmar health del estado anterior
