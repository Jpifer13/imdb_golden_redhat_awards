from app import db

class Director(db.Model):
    director_name = db.Column(db.String(64), primary_key=True)
    movie_name = db.Column(db.String(64), db.ForeignKey('movie.movie_name'), unique=True)
    facebook_likes = db.Column(db.Integer)

    def __repr__(self):
        return '<Director {}>'.format(self.director_name)

class Actor(db.Model):
    actor_name = db.Column(db.String(64), primary_key=True)
    movie_name = db.Column(db.String(64), db.ForeignKey('movie.movie_name'), unique=True)
    facebook_likes = db.Column(db.Integer)

    def __repr__(self):
        return '<Actor {}>'.format(self.actor_name) 

class Movie(db.Model):
    movie_name = db.Column(db.String(64), primary_key=True)
    actor_name = db.Column(db.String(64), db.ForeignKey('actor.actor_name'), unique=True)
    director_name = db.Column(db.String(64), db.ForeignKey('director.director_name'), unique=True)
    color = db.Column(db.String(20))
    facebook_likes = db.Column(db.Integer)
    num_critic_for_reviews = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    gross = db.Column(db.Integer)
    genres = db.Column(db.String(64))
    num_voted_users = db.Column(db.Integer)
    cast_total_facebook_likes = db.Column(db.Integer)
    facenumber_in_poster = db.Column(db.Integer)
    plot_keywords = db.Column(db.String(64))
    movie_imdb_link = db.Column(db.String(64))
    num_user_for_reviews = db.Column(db.String(64))
    language = db.Column(db.String(64))
    country = db.Column(db.String(64))
    content_rating = db.Column(db.String(64))
    budget = db.Column(db.Integer)
    title_year = db.Column(db.Integer)
    imdb_score = db.Column(db.Float)
    aspect_ratio = db.Column(db.Float)
    movie_facebook_likes = db.Column(db.Integer)

    def __repr__(self):
        return '<Movie {}>'.format(self.movie_name) 