from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["item"])
async def read_item():
    return {"item": "这是item"}
