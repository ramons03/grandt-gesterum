# Proyecto: marketup-sales

Stack: Node API + frontend web + Postgres.

## Objetivos
- auth segura en produccion,
- deshabilitar rutas de desarrollo,
- reproducibilidad de build/deploy.

## Checklist
- `NODE_ENV=production`,
- `ALLOW_DEV_LOGIN=false`,
- smoke `/config`, `/auth/dev-login`, `/health`.
