from fastapi import APIRouter
from pydantic import BaseModel

from app.sql_app.curd.user import *
from app.utils.status_code import *

router = APIRouter()


class User(BaseModel):
    name: str
    password: str


@router.get("/list", tags=["users"],summary="获取用户列表")
async def read_users():
    user_list = []
    for item in get_all_users():
        user_list.append({
            "id": item.id,
            "username": item.username,
        })
    return {
        "code": ResponseSuccess.code,
        "msg": ResponseSuccess.message,
        "data": user_list
    }


# 新增用户
@router.post("/add", tags=["users"],summary="新增用户")
async def add_user(user: User):
    if insert_user(user.name, user.password):
        return {"code": ResponseSuccess.code, "msg": ResponseSuccess.message}
    else:
        return {"code": ResponseError.code, "msg": ResponseError.message}
