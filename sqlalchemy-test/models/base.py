from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = 'sqlite:///test.db'
engine = create_engine(DB_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)
Base = declarative_base()

def init_db():
    Base.metadata.drop_all(engine) # drop all data
    Base.metadata.create_all(engine)


class ModelBase(Base):
    __abstract__ = True
    session = Session()
    