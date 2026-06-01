# Proyecto: estudio-contable

Stack: ASP.NET Core + SQLite + Nginx reverse proxy.

## Objetivos operativos
- estabilidad de arranque sin systemd,
- consistencia DB sin romper produccion,
- rutas contables y permisos funcionales.

## Checklist rapido
- precheck puertos 5043/7051,
- run script `start_estudio_contable.sh`,
- validar `/health`, `/version`, login admin.
