import os
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import PyJWKClient

security = HTTPBearer()
issuer = os.environ["KEYCLOAK_ISSUER"]
jwks_client = PyJWKClient(os.environ["KEYCLOAK_JWKS_URL"])

def current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    signing_key = jwks_client.get_signing_key_from_jwt(token)
    claims = jwt.decode(
        token,
        signing_key.key,
        algorithms=["RS256"],
        issuer=issuer,
        options={"verify_aud": False},
    )
    roles = claims.get("realm_access", {}).get("roles", [])
    if "app-user" not in roles:
        raise HTTPException(status_code=403, detail="app-user role required")
    return {"username": claims.get("preferred_username"), "roles": roles}
