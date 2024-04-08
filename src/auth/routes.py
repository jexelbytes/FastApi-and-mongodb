from fastapi import APIRouter
from .schemas import LoginCreds
from .controllers import loginapp, refresh

router = APIRouter()

@router.post('/Login')
async def get_token(auth: LoginCreds) -> dict: return await loginapp(auth=auth)

@router.post('/Refresh')
async def refresh_token(refresh_token:str) -> dict: return await refresh(refresh=refresh_token)
