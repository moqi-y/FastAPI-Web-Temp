### 目录结构
```
.
├── app                  # 「app」是一个 Python 包
│    ├── __init__.py      # 这个文件使「app」成为一个 Python 包
│    ├── main.py          # 「main」模块，例如 import app.main
│    ├── dependencies.py  # 「dependencies」模块，例如 import app.dependencies
│    └── routers          # 「routers」是一个「Python 子包」
│    │   ├── __init__.py  # 使「routers」成为一个「Python 子包」
│    │   ├── items.py     # 「items」子模块，例如 import app.routers.items
│    │   └── users.py     # 「users」子模块，例如 import app.routers.users
│    └── middleware
│    │   ├── __init__.py
│    │   └── cors.py      # 跨域配置
│    └──sql_app           # 数据库配置
│    │   ├── __init__.py
│        │   └── models.py    # 数据库模型
│        └── database.py   # 数据库连接
│    └──utils           # 工具函数
│    │   ├── __init__.py
│    │   └── status_code.py # 状态码

```

## 安装依赖
**python版本：** 3.10.11

```bash
pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirements.txt
```
## 运行
```bash
uvicorn app.main:app --reload
```
## 接口文档
http://127.0.0.1:8000/docs

## pip国内源
- 阿里云：http://mirrors.aliyun.com/pypi/simple/
- 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
- 华中理工大学：http://pypi.hustunique.com/
- 山东理工大学：http://pypi.sdutlinux.org/
- 豆瓣：http://pypi.douban.com/simple/
