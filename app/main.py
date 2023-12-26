import uvicorn
from fastapi import Depends, FastAPI

from app.dependencies import get_query_token, get_token_header
from app.routers import users
import config

app = FastAPI(
    title="FastAPI",
    description="FastAPI-Web-Temp接口文档",
    version="1.0.0",
    # dependencies=[Depends(get_query_token)]  # 全部接口的依赖项
)

app.include_router(
    users.router,
    prefix="/users",  # 路径名
    tags=["users"],  # 文档标签名
    dependencies=[Depends(get_token_header)],  # 依赖项
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    # 读取.env中的配置
    print(config.APP_NAME)
    return {
        "message": "Hello Bigger Applications!",
        "data": {
            "appName": config.APP_NAME,
            "appVersion": config.APP_VERSION
        }
    }
