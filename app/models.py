from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from app.config import Base

class Movie(Base):
    __tablename__ = 'movies'
    movie_name = Column(String(64), primary_key=True)
    actor_1_name = Column(String(64), ForeignKey('actors.actor_name'), unique=True)
    actor_2_name = Column(String(64), ForeignKey('actors.actor_name'), unique=True)
    actor_3_name = Column(String(64), ForeignKey('actors.actor_name'), unique=True)
    director_name = Column(String(64), ForeignKey('directors.director_name'), unique=True)
    color = Column(String(20))
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
        return(
        """<Movie(movie_name='{}',
        actor_1_name='{}',
        actor_2_name='{}',
        actor_3_name='{}',
        director_name='{}',
        color='{}',
        num_critic_for_reviews={},
        duration={},
        gross={},
        genres='{}',
        num_voted_users={},
        cast_total_facebook_likes={},
        facenumber_in_poster={},
        plot_keywords='{}',
        num_user_for_reviews={},
        language='{}',
        country='{}',
        budget={},
        title_year={},
        imdb_score={},
        aspect_ratio={},
        movie_facebook_likes={})>""".format(
            self.movie_name,
            self.actor_1_name,
            self.actor_2_name,
            self.actor_3_name,
            self.director_name,
            self.color,
            self.num_critic_for_reviews,
            self.duration,
            self.gross,
            self.genres,
            self.num_voted_users,
            self.cast_total_facebook_likes,
            self.facenumber_in_poster,
            self.plot_keywords,
            self.num_user_for_reviews,
            self.language,
            self.country,
            self.budget,
            self.title_year,
            self.imdb_score,
            self.aspect_ratio,
            self.movie_facebook_likes)
        )
class Director(Base):
    __tablename__ = 'directors'
    director_name = Column(String(64), primary_key=True)
    movie_name = Column(String(64), ForeignKey('movies.movie_name'), unique=True)
    facebook_likes = Column(Integer)

    def __repr__(self):
        return "<Director(director_name='{}', movie_name='{}', facebook_likes={})>".format(self.director_name, self.movie_name, self.facebook_likes)

class Actor(Base):
    __tablename__ = 'actors'
    actor_name = Column(String(64), primary_key=True)
    movie_name = Column(String(64), ForeignKey('movies.movie_name'), unique=True)
    facebook_likes = Column(Integer)

    def __repr__(self):
        return "<Actor(actor_name='{}', movie_name='{}', facebook_likes={})>".format(self.actor_name, self.movie_name, self.facebook_likes) 

