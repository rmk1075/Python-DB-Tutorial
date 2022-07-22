from models.base import ModelBase
from sqlalchemy import Column, Integer, String


class User(ModelBase):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f'<User::id={self.id} user_id={self.user_id} name={self.name}>'
