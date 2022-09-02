from models.base import ModelBase
from models.team import Team
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(ModelBase):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    team_id = Column(Integer, ForeignKey("team.id"))
    team = relationship("Team", back_populates="users")

    def __repr__(self):
        return f'<User::id={self.id} user_id={self.user_id} name={self.name} team_id={self.team_id} team={self.team.id}>'
    
    @classmethod
    def get_by_user_id(cls, user_id: str=str()):
        user = cls.session.query(cls).filter(cls.user_id == user_id).first()
        return user