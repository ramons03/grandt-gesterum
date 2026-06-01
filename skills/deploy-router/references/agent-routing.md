# Agent Routing for Deploys

## Matriz principal
- .NET / ASP.NET / Roslyn -> agent.dotnet
- Linux / nginx / system services -> agent.linux
- Frontend React/Vue -> agent.frontend
- CI/CD / release / artifacts -> agent.devops-cicd
- Python backend/scripts -> agent.python

## Reglas multiagente
1. Priorizar riesgo de produccion.
2. Lider por dominio dominante.
3. Incluir agent.linux cuando se toca Nginx/host.

## Entregable por agente
- cambios,
- validaciones,
- riesgos,
- rollback.
