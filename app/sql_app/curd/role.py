from sqlalchemy.orm import sessionmaker, exc

from app.sql_app.database import Base, engine
from app.sql_app.models import Role

# 创建数据表
Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()


# 查询所有权限
def get_all_permissions():
    try:
        permissions = session.query(Role).all()
        return permissions
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        session.close()


# 新增权限
def insert_permission(name, permissions, remark=""):
    perm = Role(name=name, permissions=permissions, remark=remark)
    try:
        session.add(perm)
        session.commit()
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
    finally:
        session.close()


# 调用函数获取所有权限
if __name__ == '__main__':
    all_permissions = get_all_permissions()
    for permission in all_permissions:
        print(permission.name)
