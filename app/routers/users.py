from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["users"])
async def read_users():
    return {
        "code": 200,
        "msg": "success",
        "data": [{"username": "fakeuser1"}, {"username": "fakeuser2"}]
    }


@router.get("/info", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
