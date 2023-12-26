.

├── aerich.ini

├── app                                                       # 代码主目录

│   ├── commons                                               # 一些逻辑

│   │   ├── 

│   │   └── 

│   ├── 

│   ├── logs                                                  # 日志配置目录

│   │   ├── 

│   ├── middleware                                            # 中间件配置目录

│   │   ├── 

│   ├── models                                                # 数据模型目录

│   │   ├── 

│   │   ├── model.py

│   ├── mydbs                                                 # 数据库相关目录

│   │   ├── database.py

│   │   ├── 

│   │   └── 

│   ├── 

│   │   └── 

│   ├── routers                                               # 路由视图目录

│   │   ├── 

│   │   ├── 

│   ├── schemas                                               # 参数校验模型

│   │   ├── 

│   │   └── 

│   └── utils                                                 # 工具目录

│       ├── common\_util.py

│       ├── constant.py

│       ├── fake\_data.py

│       ├── 

│       ├── phone\_code.py

│       ├── qiniu\_sdk\_python.py

│       └── tencentcloud\_sdk\_python.py

├── config.py                                                    # 配置文件，包含生产，测试，开发三套配置

├── create\_table.sql                                             # 建表sql

├── deploy.sh                                                    # docker镜像构建

├── docker-compose.yaml                                          # docker容器编排管理

├── Dockerfile                                                   # 构建镜像配置文件

├── main.py                                                      # 程序启动文件

├── migrations                                                   # 数据库管理文件

│   └── models

│       ├── 0\_202056062220145621\_init.json

│       └── old\_models.py

├── pip.conf                                                     # pip配置

├── prestart.sh                                                  # docker启动时自动执行数据库迁移脚本

├── README.md                                                    # 程序文档

├── requirements.txt                                             # 依赖环境

└── run.sh                                                       # 启动docker容器


