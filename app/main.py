import uvicorn
from fastapi import FastAPI

import config
from app.middleware import cors
from app.routers import router_config

app = FastAPI(
    title="FastAPI",
    description="FastAPI-Web-Temp接口文档",
    version="1.0.0",
    # dependencies=[Depends(get_query_token)]  # 全部接口的依赖项
)

#  跨域设置
cors.cors_config(app)

# 路由配置
router_config(app)


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
