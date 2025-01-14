from sqlalchemy import create_engine, orm

from models import Base

DB = "postgresql://postgres:12345@localhost:5432/postgres_ino"

engine = create_engine(DB, echo=True)

Base.metadata.create_all(engine)

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)