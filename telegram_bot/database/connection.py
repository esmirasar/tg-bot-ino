from sqlalchemy import create_engine, orm

from .models import Base


DB = "postgresql://postgres_user:12345@bot_database:5432/postgres_name"

engine = create_engine(DB, echo=True)

Base.metadata.create_all(engine)

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)