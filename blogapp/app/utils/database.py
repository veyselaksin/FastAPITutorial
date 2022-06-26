from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

def set_engine(host, port, user, password, db):
    url = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}".format(host=host, port=port, user=user, password=password, db=db)

    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)

    return engine

def get_engine():
    engine = set_engine(
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        db=os.environ.get("DB_NAME")
    )
    
    return engine

def get_session():
    engine = set_engine(
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        db=os.environ.get("DB_NAME")
    )

    session = sessionmaker(bind=engine)()
    return session

def get_db():
    db = get_session()

    try:
        yield db
    except Exception as ex:
        raise ex
    finally:
        db.close()

Base = declarative_base()
