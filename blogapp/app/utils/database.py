from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import psycopg2


def get_engine(user, password, host, port, db):
    url = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}".format(user=user, password=password, host=host, port=port, db=db)

    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)

    return engine


def get_session():
    engine = get_engine()

    session = sessionmaker(bind=engine)()
    return session
