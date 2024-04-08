from fastapi import Request
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials
from .exceptions import ExpiredTokenException
from .controllers import decodeJWT
from .schemas import ActiveSession
from datetime import datetime

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class jwtBearer(HTTPBearer):
  
  def __init__(self, auto_Error : bool = True):
    super(jwtBearer, self).__init__(auto_error=auto_Error)

  async def __call__(self, request : Request) -> ActiveSession:
    credentials: HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
    session = await self.verify_jwt(credentials.credentials)
    if session:
        return session
    else:
        raise ExpiredTokenException()
    
  async def verify_jwt(self, jwtoken : str) -> ActiveSession:
    payload = await decodeJWT(jwtoken)
    if datetime.strptime(payload['expiry'], '%y-%m-%d %H:%M:%S') > datetime.now():
        session = await ActiveSession.find_one({"token":jwtoken})
        if session:
            return session
    
    return False
