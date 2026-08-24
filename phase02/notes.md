# Phase 02 Notes

- Compose defines services, networks, volumes, health checks, and dependencies.
- Service names provide DNS inside phase02-net.
- PostgreSQL, pgAdmin, and Redis data use named volumes.
- Runtime credentials come from .env and are not committed.
- Nginx exposes one entry point and routes frontend and /api requests.
- FastAPI uses /api/health consistently for direct, proxy, and health-check access.
- Health checks separate container running state from service readiness.
- The validated frontend build reported zero npm vulnerabilities.
