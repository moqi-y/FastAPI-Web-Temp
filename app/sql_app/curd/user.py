from sqlalchemy.orm import sessionmaker, exc

from app.sql_app.database import Base, engine
from app.sql_app.models import User

# 创建数据表
Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()


# 插入数据
def insert_user(username, password):
    user = User(username=username, password=password)
    try:
        session.add(user)
        session.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
        raise e
    finally:
        session.close()

    # 条件查询数据


def get_user(user_id):
    try:
        user = session.query(User).filter_by(id=user_id).first()
        return user
    except exc.NoResultFound:
        return None
    finally:
        session.close()


def get_all_users():
    try:
        users = session.query(User).all()
        print("users", users)
        return users
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        session.close()


# 测试代码
# if __name__ == '__main__':
    # user_list = []
    # for item in get_all_users():
    #     user_list.append({
    #         "id": item.id,
    #         "username": item.username,
    #     })
    # print("user_list", user_list)
    # insert_user("admin", "123456")
