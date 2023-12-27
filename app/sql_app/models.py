# 定义数据表模型
from sqlalchemy import *
from app.sql_app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
