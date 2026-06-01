# Current Topology Reference

## Patrones existentes
- Vhost principal: `eldean.com.ar` con subrutas proxied.
- Vhost contable: `contable.eldean.com.ar` hacia `127.0.0.1:5043`.
- Patrón reverse proxy:
  - `proxy_set_header Host $host`
  - `proxy_set_header X-Real-IP $remote_addr`
  - `proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for`
  - `proxy_set_header X-Forwarded-Proto $scheme`

## Ubicaciones relevantes (host)
- `/etc/nginx/sites-available/`
- `/etc/nginx/sites-enabled/`

## Flujo recomendado
1) backup de vhost actual
2) editar vhost destino
3) `nginx -t`
4) `systemctl reload nginx`
5) `curl --resolve host:80:127.0.0.1 http://host/`
6) validar logs de error si falla

## Rollback rapido
- restaurar archivo backup
- `nginx -t`
- `systemctl reload nginx`
