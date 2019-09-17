from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from app.config import Base

class Movie(Base):
    __tablename__ = 'movies'
    movie_name = Column(String(64), primary_key=True)
    actor_name = Column(String(64), ForeignKey('actors.actor_name'), unique=True)
    director_name = Column(String(64), ForeignKey('directors.director_name'), unique=True)
    color = Column(String(20))
    facebook_likes = Column(Integer)
    num_critic_for_reviews = Column(Integer)
    duration = Column(Integer)
    gross = Column(Integer)
    genres = Column(String(64))
    num_voted_users = Column(Integer)
    cast_total_facebook_likes = Column(Integer)
    facenumber_in_poster = Column(Integer)
    plot_keywords = Column(String(64))
    movie_imdb_link = Column(String(64))
    num_user_for_reviews = Column(String(64))
    language = Column(String(64))
    country = Column(String(64))
    content_rating = Column(String(64))
    budget = Column(Integer)
    title_year = Column(Integer)
    imdb_score = Column(Float)
    aspect_ratio = Column(Float)
    movie_facebook_likes = Column(Integer)

    def __repr__(self):
        return '<Movie {}>'.format(self.movie_name) 

class Director(Base):
    __tablename__ = 'directors'
    director_name = Column(String(64), primary_key=True)
    movie_name = Column(String(64), ForeignKey('movies.movie_name'), unique=True)
    facebook_likes = Column(Integer)

    def __repr__(self):
        return '<Director {}>'.format(self.director_name)

class Actor(Base):
    __tablename__ = 'actors'
    actor_name = Column(String(64), primary_key=True)
    movie_name = Column(String(64), ForeignKey('movies.movie_name'), unique=True)
    facebook_likes = Column(Integer)

    def __repr__(self):
        return '<Actor {}>'.format(self.actor_name) 
