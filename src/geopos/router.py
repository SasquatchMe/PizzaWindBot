from fastapi import APIRouter
from fastapi.params import Depends

from src.geopos.repo import GeoPosRepo
from src.geopos.schemas import SGeoPos, SAddGeoPos

router = APIRouter(
    prefix="/geopos",
)


@router.post("")
async def add_one_geopos(geopos: SAddGeoPos = Depends(SAddGeoPos)):
    geopos_id = await GeoPosRepo.add_one(geopos)
    return {"status": "ok", "geopos_id": geopos_id}


@router.get("")
async def get_all_geopos() -> dict[str, list[SGeoPos]]:
    geoposes = await GeoPosRepo.get_all()
    return {"geoposes": geoposes}


@router.get("/random/{value}")
async def get_random_geopos(value: int) -> list[SGeoPos]:
    geoposes = await GeoPosRepo.get_random_geopos(value)
    return geoposes
