import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv


load_dotenv()


HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
SSL_CA = os.getenv("SSL_CA")

# SQLAlchemy connection URL
DATABASE_URL = (
    f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    f"?ssl_ca={SSL_CA}"
)

# Create engine
engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
