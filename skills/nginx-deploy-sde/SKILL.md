---
name: nginx-deploy-sde
description: Despliega y valida aplicaciones .NET/Node detras de Nginx siguiendo el patron existente en eldean/sde-cobros/estudio-contable, con secuencia precheck-ejecucion-verificacion-rollback y controles de puerto, proxy_pass, TLS y healthcheck.
---

# nginx-deploy-sde

## Procedimiento
1. Cargar `references/current-topology.md`.
2. Ejecutar precheck de puertos, procesos, vhosts y certificados.
3. Aplicar o crear server block Nginx segun plantilla.
4. Validar `nginx -t` y recargar servicio.
5. Verificar endpoint local y publico (si aplica).
6. Entregar rollback exacto.

## Reglas
- no sobrescribir configuracion existente sin backup.
- mantener consistencia con patrones actuales (`contable.eldean.com.ar`, subpaths y proxy headers).
- si hay riesgo de downtime, aplicar despliegue en ventana controlada.

## Salida minima
- archivos tocados,
- comandos ejecutados,
- estado antes/despues,
- pruebas HTTP,
- rollback listo para copiar.
