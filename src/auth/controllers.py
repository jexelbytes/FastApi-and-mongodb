from config import JWT_SECRET, JWT_ALGORITHM, JWT_EXPIRE_TIME, JWT_REFRESH_EXPIRE_TIME
from .exceptions import ExpiredRefreshException, InvalidTokenException
from users.exceptions import UserNotFoundException
from .schemas import ActiveSession, LoginCreds
from datetime import datetime, timedelta
from users.documents import User
import jwt

async def loginapp(auth:LoginCreds) -> dict:
    user = await User.find_one(auth.model_dump())
    if not user:
        raise UserNotFoundException()
    return await signJWT(user=user)

async def logoutapp() -> dict:
  pass

async def signJWT(user: User) -> dict:
  
  expire_time = datetime.now() + timedelta(minutes=JWT_EXPIRE_TIME)
  expire_refresh = datetime.now() + timedelta(minutes=JWT_REFRESH_EXPIRE_TIME)
  
  payload = {
    "userEmail": user.email,
    "expiry": expire_time.strftime('%y-%m-%d %H:%M:%S')
  }
  
  token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
  
  payload['expiry'] = expire_refresh.strftime('%y-%m-%d %H:%M:%S')
  
  refresh = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
  
  this_session = ActiveSession(
    user_id=user.id,
    token=token,
    expire_at=expire_time
  )
  await this_session.create()
  
  return { 'access_token': token, 'refresh': refresh }

async def refresh(refresh:str) -> dict:
  payload = await decodeJWT(token=refresh)
  
  if datetime.strptime(payload['expiry'], '%y-%m-%d %H:%M:%S') > datetime.now():
    raise ExpiredRefreshException()
  
  user = await User.find_one({"email":payload['userEmail']})
  return await signJWT(user=user)
  
async def decodeJWT(token: str) -> dict:
  try:
    decode_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
    return decode_token
  except Exception as err:
    print(f"Unexpected: {err}")
    raise InvalidTokenException()
