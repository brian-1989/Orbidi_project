from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "kOMINsYQbLsLIYnAzBlWdaBHsvHHIGjM"
POSTGRES_HOST = "viaduct.proxy.rlwy.net"
POSTGRES_PORT = "44453"
POSTGRES_DB = "railway"

DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
            POSTGRES_USER,
            POSTGRES_PASSWORD,
            POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB)


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
