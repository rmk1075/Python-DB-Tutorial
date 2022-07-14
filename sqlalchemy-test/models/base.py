from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = 'sqlite:///test.db'
engine = create_engine(DB_URL) # Engine 객체를 반환한다. Engine 은 SQLAlchemy 의 connection pool 과 Dialect 를 참조하여 실제 DB 연결과 DB API 를 제공한다.
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True) # 새로운 Session 객체를 생성한다.
Base = declarative_base() # Declarative Mapping 을 위한 Base 클래스를 생성한다. 해당 클래스를 상속받은 클래스들에게 declarative mappping 이 적용된다.

def init_db():
    # Base.metadata: MetaData 객체이다. Table 객체와 관련된 스키마 생성자의 모음.
    Base.metadata.drop_all(engine) # 해당 meatadata 에 저장되어 있는 모든 테이블들을 삭제한다.
    Base.metadata.create_all(engine) # 해당 metadata 에 저장되어 있는 모든 테이블들을 생성한다.


class ModelBase(Base):
    __abstract__ = True
    session = Session()
    