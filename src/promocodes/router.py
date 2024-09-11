from fastapi import APIRouter
from fastapi.params import Depends

from src.promocodes.repo import PromocodesRepo
from src.promocodes.schemas import SPromocodeAdd

router = APIRouter(prefix="/promocodes", tags=["promocodes"])


@router.post("")
async def add_one(promocode_data: SPromocodeAdd):
    promocode = await PromocodesRepo.add_one(promocode_data)
    return promocode


@router.patch("/deactivate/{promocode_id}")
async def deactivate_one(promocode_id: int):
    promocode = await PromocodesRepo.deactivate_promocode(promocode_id)
    return promocode


@router.get("/{code}")
async def get_by_code(code: str):
    promocode = await PromocodesRepo.get_one_by_code(code)
    return promocode
