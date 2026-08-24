# Phase 02 Docker Compose Web System

## Services
- Application: http://localhost:8080/
- API documentation: http://localhost:8000/docs
- pgAdmin: http://localhost:5050/
- PostgreSQL: internal service db:5432
- Redis: internal service redis:6379

## Start
1. Copy .env.example to .env and set local values.
2. Run: docker compose --project-name phase02 config --quiet
3. Run: docker compose --project-name phase02 build
4. Run: docker compose --project-name phase02 up --detach

## Health endpoint
- Direct: http://localhost:8000/api/health
- Via Nginx: http://localhost:8080/api/health

## Resources
- Network: phase02-net
- Volumes: phase02-postgres-data, phase02-pgadmin-data, phase02-redis-data
