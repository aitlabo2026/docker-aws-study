# Phase 03 Auth Worker Queue Monitoring

## URLs
- Application: http://localhost:8080/
- API docs: http://localhost:8000/docs
- Keycloak: http://localhost:8081/
- pgAdmin: http://localhost:5050/
- Prometheus: http://localhost:9090/
- Grafana: http://localhost:3000/

## Flows
- Authentication: React -> Keycloak -> JWT -> FastAPI
- Async: FastAPI -> Redis broker -> Celery Worker -> Redis result backend
- Monitoring: FastAPI metrics -> Prometheus -> Grafana

## Start
1. Prepare .env from .env.example.
2. docker compose --project-name phase03 config --quiet
3. docker compose --project-name phase03 build
4. docker compose --project-name phase03 up --detach
