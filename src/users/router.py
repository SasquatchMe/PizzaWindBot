from fastapi import APIRouter
from fastapi.params import Depends

from src.users.repo import UserRepo
from src.users.schemas import SAddUser, SUser, SGetUserById, SDeleteUser

router = APIRouter(
    prefix='/users',
)

@router.get('')
async def read_users() -> dict[str, list[SUser]]:
    users = await UserRepo.get_all()
    return {'users': users}

@router.post('')
async def create_user(user: SAddUser = Depends(SAddUser)) -> dict:
    user_id = await UserRepo.add_one(user)
    return {'status': 'OK', 'user_id': user_id}

@router.get('/{user_id}')
async def get_user(find_user: SGetUserById = Depends(SGetUserById)) -> dict[str, SUser]:
    user = await UserRepo.get_one(find_user)
    return {'user': user}

@router.delete('/{user_id}')
async def delete_user(find_user: SDeleteUser = Depends(SDeleteUser)) -> dict:
    user = await UserRepo.delete_user(find_user)
    return {'status': 'OK', 'user_id': user}