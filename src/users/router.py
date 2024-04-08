from beanie import PydanticObjectId
from fastapi import APIRouter, Depends
from .schemas import UpdateUser, CreateUser
from auth.schemas import ActiveSession
from auth.dependencies import jwtBearer
from .controllers import get_all_users, get_user_by_id, create_user, update_user
router = APIRouter()


@router.get('/my_profile')
async def get_profile(session:ActiveSession = Depends(jwtBearer())): return await get_user_by_id(session.user_id)

@router.get('/user')
async def get_users(): return await get_all_users()

@router.get('/user{id}')
async def get_users(id:PydanticObjectId): return await get_user_by_id(id=id)

@router.post('/user')
async def add_user(user: CreateUser): return await create_user(user=user)

@router.put("/user/{id}")
async def update_user_data(id: PydanticObjectId, req: UpdateUser): return await update_user(id=id, req=req)