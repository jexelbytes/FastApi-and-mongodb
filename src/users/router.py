from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List
from .schemas import User, UpdateUser
from .controllers import get_all_users, create_user, update_user


router = APIRouter()


@router.get('/user')
async def get_users(): return await get_all_users()

@router.post('/user')
async def add_user(user: User): return await create_user(user=user)

@router.put("/user/{id}")
async def update_user_data(id: PydanticObjectId, req: UpdateUser): return await update_user(id=id, req=req)