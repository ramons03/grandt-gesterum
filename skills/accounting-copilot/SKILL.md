---
name: accounting-copilot
description: Soporte contable-operativo para productos SaaS con foco en libro diario/mayor, estados financieros, devengo, ajustes y metricas financieras aplicables al negocio. Usar cuando se necesite traducir operaciones del sistema a informacion contable util para gestion y toma de decisiones.
---

# accounting-copilot

## Procedimiento
1. Cargar fuentes en `references/accounting-map.md`.
2. Mapear eventos de negocio a asientos contables.
3. Verificar impacto en:
   - Estado de resultados
   - Balance general
   - Flujo de efectivo
4. Entregar recomendaciones de control interno y automatizacion.

## Salida minima
- asiento propuesto (debe/haber)
- criterio (devengo/realizacion)
- riesgo contable
- validacion requerida
