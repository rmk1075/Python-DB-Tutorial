from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import traceback


# DB_URL = 'sqlite:///test.db'
DB_URL = 'sqlite:///:memory:' # in-memory database 사용
engine = create_engine(DB_URL) # Engine 객체를 반환한다. Engine 은 SQLAlchemy 의 connection pool 과 Dialect 를 참조하여 실제 DB 연결과 DB API 를 제공한다.
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True) # 새로운 Session 객체를 생성한다.
Base = declarative_base() # Declarative Mapping 을 위한 Base 클래스를 생성한다. 해당 클래스를 상속받은 클래스들에게 declarative mappping 이 적용된다.

def init_db():
    # Base.metadata: MetaData 객체이다. Table 객체와 관련된 스키마 생성자의 모음.
    # Base.metadata.drop_all(engine) # 해당 meatadata 에 저장되어 있는 모든 테이블들을 삭제한다.
    Base.metadata.create_all(engine) # 해당 metadata 에 저장되어 있는 모든 테이블들을 생성한다.


class ModelBase(Base):
    __abstract__ = True
    session = Session()
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True) # autoincremented id for every database table
    
    @classmethod
    def _exec(cls, method: any, **kwargs):
        try:
            result = method(cls.session, **kwargs)
            cls.session.commit()
        except Exception as e:
            print(traceback.print_exc())
            result = None
            cls.session.rollback()
        return result
    
    @classmethod
    def _read(cls, session: Session, id: any):
        return session.query(cls).filter(cls.id == id).first()
    
    @classmethod
    def _read_all(cls, session: Session):
        return session.query(cls).all()
    
    @classmethod
    def _add(cls, session: Session, obj: any):
        session.add(obj)
        return obj

    @classmethod
    def _delete(cls, session: Session, obj: any):
        session.delete(obj)
    
    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        return cls._exec(cls._add, obj=obj)
    
    @classmethod
    def get(cls, id: any):
        return cls._exec(cls._read, id=id)
    
    @classmethod
    def get_all(cls):
        return cls._exec(cls._read_all)
    
    @classmethod
    def update(cls, obj: any):
        return cls._exec(cls._add, obj=obj)
    
    @classmethod
    def delete(cls, obj: any):
        return cls._exec(cls._remove, obj=obj)
