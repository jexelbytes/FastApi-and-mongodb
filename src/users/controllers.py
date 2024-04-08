from beanie import PydanticObjectId
from fastapi import HTTPException
from .schemas import User, UpdateUser, CreateUser
from .exceptions import UserNotFoundException

async def get_user_by_id(id: PydanticObjectId) -> User:
    user = await User.get(id)
    if not user:
        raise UserNotFoundException()
    else:
        return user

async def get_all_users() -> list[User]:
    return await User.find_all().to_list()

async def create_user(user: CreateUser) -> User:
    user = User(**user.model_dump())
    return await user.create()

async def update_user(id: PydanticObjectId, req: UpdateUser) -> User:
    update_query = {"$set": req.model_dump(exclude_none=True)}
    user = await get_user_by_id(id)
    await user.update(update_query) 
    return user