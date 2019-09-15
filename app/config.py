import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
basedir = os.path.abspath(os.path.dirname(__file__))
Base = declarative_base()

class Config(object):
    """
    This class configures the database and its migrations
    """

    def recreate_database(Base, engine):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    #Looks for url to database if not creates or uses local db file. Since this project is small I am just using a local db file
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    
    url = SQLALCHEMY_DATABASE_URI
    engine = create_engine(url)
    recreate_database(Base, engine)
    Session = sessionmaker(bind=engine)
    
    
