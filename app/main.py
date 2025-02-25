import uvicorn
from fastapi import FastAPI
from app.utils.status_code import *
import config
from app.middleware import cors
from app.routers import router_config
from fastapi import applications
from fastapi.openapi.docs import get_swagger_ui_html


def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url="https://cdn.bootcdn.net/ajax/libs/swagger-ui/5.1.0/swagger-ui-bundle.min.js",
        swagger_css_url="https://cdn.bootcdn.net/ajax/libs/swagger-ui/5.1.0/swagger-ui.min.css"
    )


applications.get_swagger_ui_html = swagger_monkey_patch

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
@app.get("/ping", summary="连通测试", description="测试连通性", tags=["测试"])
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
