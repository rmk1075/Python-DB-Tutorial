from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = None
Session = None
Base = declarative_base()

def init_db():
    engine = create_engine('sqlite:///test.db')
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)
    Base.metadata.create_all(engine)


class ModelBase(Base):
    __abstract__ = True
    