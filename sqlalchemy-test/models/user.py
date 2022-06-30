from models.base import ModelBase
from sqlalchemy import Column, Integer, String


class User(ModelBase):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = Column(String, nullable=False)
    name = Column(String, nullable=False)  

    @classmethod
    def get(cls, **kwargs):
        users = cls.session.query(cls).all()
        return users

    @classmethod
    def create(cls, user_id: str, name: str):
        user = cls(user_id=user_id, name=name)
        cls.session.add(user)
        return user

