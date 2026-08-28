# Phase 04 Docker Operations
## Scope
- Health checks for 10 services
- Docker json-file logs with 10m x 3 rotation
- PostgreSQL custom-format backup and isolated restore verification

## Compose
docker compose --project-name phase04 --file compose.yaml --file compose.operation.yaml up --detach --build

## URLs
- App: http://localhost:8080/
- API docs: http://localhost:8000/docs
- Keycloak: http://localhost:8081/
- Prometheus: http://localhost:9090/targets
- Grafana: http://localhost:3000/
- pgAdmin: http://localhost:5050/

## Data
- Named volumes provide runtime persistence.
- backups/phase04-appdb.dump is a portable logical backup and is not tracked by Git.
- Restore verification uses a separate timestamped database.