from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.settings import Settings

settings = Settings()


engine = create_engine(settings.get_db_url(), connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    except Exception as e:
        raise e
    finally:
        db.close()