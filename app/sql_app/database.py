import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

# 连接数据库
engine = create_engine("mysql+pymysql://root:123456@localhost:3306/fastapi_web_temp", echo=True)
Base = sqlalchemy.orm.declarative_base()


# 定义数据表模型
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)


# 创建数据表
Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

# 插入数据
user1 = User(name="李华", age=25)
user2 = User(name="张三", age=30)
session.add_all([user1, user2])
session.commit()

# 查询数据
users = session.query(User).all()
for user in users:
    print(user.name, user.age)

# 关闭会话
session.close()
