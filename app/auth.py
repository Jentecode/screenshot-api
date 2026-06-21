from fastapi.security import APIKeyHeader
from fastapi import HTTPException, Depends
from app.config import settings


header_scheme = APIKeyHeader(name="X-API-Key")

async def check_API(key: str = Depends(header_scheme)):
    if key in settings.API_KEYS:
        return {"key": key}
    raise HTTPException(status_code=401, detail="API key niet gevonden")
