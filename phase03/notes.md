# Phase 03 Notes

- Keycloak authenticates users and issues signed access tokens.
- React uses Authorization Code Flow with PKCE and keeps tokens in memory.
- FastAPI verifies JWT signature, issuer, expiration, and app-user role.
- Redis transports Celery jobs and stores task results.
- Worker executes jobs outside the API request process.
- Prometheus scrapes metrics and Grafana visualizes Prometheus data.
