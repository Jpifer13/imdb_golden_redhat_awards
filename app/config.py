import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    This class configures the database and its migrations
    """
    #Looks for url to database if not creates or uses local db file. Since this project is small I am just using a local db file
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False