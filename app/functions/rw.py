import csv
import io
import pandas as pd
from app.models import Director, Actor, Movie
from app import Config
import psycopg2 

def import_database():
    """
    Use Pandas to create a dataframe of given csv file.
    Then create a database table based on the first row from the frame that holds the coloumn info.
    Connect to database and commit this new table replacing one if it already exists
    """
    data = pd.read_csv("movie_metadata.csv") 

    data.head(0).to_sql('red_hat_movies', Config.engine, if_exists='replace',index=False) #truncates the table

    conn = Config.engine.raw_connection()
    cur = conn.cursor()
    output = io.StringIO()
    data.to_csv(output, sep='\t', header=False, index=False)
    output.seek(0)
    contents = output.getvalue()
    cur.copy_from(output, 'red_hat_movies', null="") # null values become ''
    conn.commit()

def insert_row(row):
    """
    This was another meathod I was trying out so that I could separate the data into better tables instead of just
    one, but time was an issue to get this project done.
    """
    session = Config.Session()
    try:
        movie = Movie(
            color=row[0],
            director_name=row[1],
            num_critic_for_reviews=int(row[2]),
            duration=int(row[3]),
            actor_2_name=row[6],
            gross=int(row[8]),
            genres=row[9],
            actor_1_name=row[10],
            movie_name=row[11],
            num_voted_users=int(row[12]),
            cast_total_facebook_likes=int(row[13]),
            actor_3_name=row[14],
            facenumber_in_poster=int(row[15]),
            plot_keywords=row[16],
            movie_imdb_link=row[17],
            num_user_for_review=row[18],
            language=row[19],
            country=row[20],
            content_rating=row[21],
            budget=int(row[22]),
            title_year=int(row[23]),
            imdb_score=float(row[25]),
            aspect_ration=float(row[26]),
            movie_facebook_likes=int(row[27])
        )
        print(movie)
        session.add(movie)
        session.commit()
    except:
        print("Movie was not added to database")
    try:
        actor_1 = Actor(
            actor_name=row[10],
            movie_name=row[11],
            facebook_likes=int(row[7])
        )
        session.add(actor_1)
        session.commit()
    except:
        print("Actor 1 was not added to database.")
    try:
        actor_2 = Actor(
            actor_name=row[6],
            movie_name=row[11],
            facebook_likes=int(row[24])
        )
        session.add(actor_2)
        session.commit()
    except:
        print("Actor 2 was not added to database.")
    try:
        actor_3 = Actor(
            actor_name=row[14],
            movie_name=row[11],
            facebook_likes=int(row[5])
        )
        session.add(actor_3)
        session.commit()
    except:
        print("Actor 3 was not added to database.")
    try:
        director = Director(
            director_name=row[1],
            movie_name=row[11],
            facebook_likes=int(row[4])
        )
        session.add(director)
        session.commit()
    except:
        print("Director was not added  to database.")
    