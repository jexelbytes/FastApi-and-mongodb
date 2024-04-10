from beanie import PydanticObjectId
from .schemas import User, UpdateUser, CreateUser
from .exceptions import UserNotFoundException
from beanie.operators import Text
import re

async def get_user_by_id(id: PydanticObjectId) -> User:
    user = await User.get(id)
    if not user:
        raise UserNotFoundException()
    else:
        return user

async def get_all_users() -> list[User]:
    return await User.find_all().to_list()

async def search_user(email:str=None, name:str=None, age:str=None, limit:int = 100, page:int = 0) -> list[User] | User:
    search = User.find_all(lazy_parse=True)
    
    if email:
        rgx = re.compile(f'.*{email}.*', re.IGNORECASE)
        search = search.find({"email" : rgx})
    
    if name:
        rgx = re.compile(f'.*{name}.*', re.IGNORECASE)
        search = search.find({"first_name":rgx})
    
    if age:
        search = search.find({"age":int(age)})
    
    return {
        "items": await search.count(),
        "page":page,
        "limit":limit,
        "data": await search.limit(limit).skip(limit*page).to_list()
    }

async def create_user(user: CreateUser) -> User:
    user = User(**user.model_dump())
    return await user.create()

async def update_user(id: PydanticObjectId, req: UpdateUser) -> User:
    update_query = {"$set": req.model_dump(exclude_none=True)}
    user = await get_user_by_id(id)
    await user.update(update_query) 
    return user