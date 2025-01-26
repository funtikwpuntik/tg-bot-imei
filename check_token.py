from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from model import Model
from gen_token import verify_token as vf

# Верификация по токену для api
async def verify_token(api_token: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    if not api_token:
        raise HTTPException(status_code=403, detail="Missing API token")

    model = Model()

    token = model.check_token(token=api_token.credentials)


    if not token or not vf(api_token.credentials, token):
        raise HTTPException(status_code=403, detail="Invalid API token")
    return api_token.credentials