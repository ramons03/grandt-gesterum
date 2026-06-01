# grandt-gesterum

Repositorio operativo de prompts, perfiles de agentes y skills para los proyectos activos.

## Objetivo
Centralizar ejecucion tecnica reproducible para:
- enrutamiento de agentes por dominio,
- runbooks por proyecto,
- skills reutilizables con criterio de validacion y rollback.

## Estructura
- `prompts/agents/`: prompts maestros por agente lider.
- `prompts/projects/`: prompt operativo por proyecto.
- `skills/`: skills reutilizables por dominio/proyecto.

## Regla de uso
1. Seleccionar agente lider por dominio.
2. Cargar prompt del proyecto.
3. Ejecutar skill correspondiente con secuencia:
   - Precheck
   - Ejecucion
   - Verificacion
   - Rollback

## Referencia de planes comerciales
Para ejecucion de ingresos, usar en paralelo:
- `/mnt/extra/devprojects/gesterum-revenue-plans`
- Repo: `https://github.com/ramons03/gesterum-revenue-plans`
