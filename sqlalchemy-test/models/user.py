from models.base import ModelBase
from sqlalchemy import Column, Integer, String


class User(ModelBase):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f'<User::id={self.id} user_id={self.user_id} name={self.name}>'

    @classmethod
    def get(cls, **kwargs):
        users = cls.session.query(cls).all()
        return users

    @classmethod
    def create(cls, user_id: str, name: str):
        user = None
        try:
            user = cls(user_id=user_id, name=name)
            cls.session.add(user)
            cls.session.commit()
        except Exception as e:
            print(traceback.format_exc())
            cls.session.rollback()
        return user
