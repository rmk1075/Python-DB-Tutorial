from models.base import ModelBase
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Team(ModelBase):
    __tablename__ = 'team'
    name = Column(String, nullable=False)
    users = relationship("User", back_populates="team")

    def __repr__(self):
        return f'<Team::id={self.id} name={self.name}>'
    