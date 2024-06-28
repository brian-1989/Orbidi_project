from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


POSTGRES_USER = config('POSTGRES_USER', cast=str)
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD', cast=str)
POSTGRES_HOST = config('POSTGRES_HOST', cast=str)
POSTGRES_PORT = config('POSTGRES_PORT', cast=str)
POSTGRES_DB = config('POSTGRES_DB', cast=str)

DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB)


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
