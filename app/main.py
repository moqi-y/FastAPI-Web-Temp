import uvicorn
from fastapi import FastAPI,status
from app.utils.status_code import *
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


# 连通测试
@app.get("/")
async def root():
    # 读取.env中的配置
    print(config.APP_NAME)
    return {
        "code": ResponseSuccess.code,
        "message": ResponseSuccess.message,
        "data": {
            "appName": config.APP_NAME,
            "appVersion": config.APP_VERSION
        }
    }
