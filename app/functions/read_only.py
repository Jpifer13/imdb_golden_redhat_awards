import pandas as pd
from app import Config
import psycopg2 

def get_data_pandas():
        """
        This is a method that uses pandaas to show data. If creating a database wasn't
        a requirement for the project pandas can be used to get all the information
        that is required.
        """ 
        data = pd.read_csv("movie_metadata.csv") 
        return data

def get_all_data_postgres():
        """
        This method returns all the data in the database
        """
        try:
                conn = Config.engine.raw_connection()
                cursor = conn.cursor()
                get_all = "select * from red_hat_movies"

                cursor.execute(get_all)
                print("Selecting all the data in the table red_hat_movies.")
                data =  cursor.fetchall()

                print("Print each row and it's columns values")
                for row in data:
                        print(
                                "color: ", row[0],
                                "director_name: ", row[1],
                                "num_critic_for_reviews: ", row[2],
                                "duration: ", row[3],
                                "director_facebook_likes: ", row[4],
                                "actor_3_facebook_likes: ", row[5],
                                "actor_2_name: ", row[6],
                                "actor_1_facebook_likes: ", row[6],
                                "gross: ", row[7],
                                "genres: ", row[8],
                                "actor_1_name: ", row[9],
                                "movie_title: ", row[10],
                                "num_voted_users: ", row[11],
                                "cast_total_facebook_likes: ", row[12],
                                "actor_3_name: ", row[13],
                                "facenumber_in_poster: ", row[14],
                                "plot_keywords: ", row[15],
                                "movie_link: ", row[16],
                                "num_users_for_review: ", row[17],
                                "language: ", row[18],
                                "country: ", row[19],
                                "content_rating: ", row[20],
                                "budget: ", row[21],
                                "title_year: ", row[22],
                                "actor_2_facebook_likes: ", row[23],
                                "imdb_score: ", row[24],
                                "aspect_ratio: ", row[25],
                                "movie_facebook_likes: ", row[26],
                        )
        except (Exception, psycopg2.Error) as error :
                print ("Error while fetching data from PostgreSQL", error)
        finally:
                #closing database connection.
                if(conn):
                        cursor.close()
                        conn.close()
                        print("PostgreSQL connection is closed")

def get_top_ten_grossest():
        """
        This method gets the top highest grossing films and returns the names of the movie
        and the amount they grossed.
        """
        try:
                conn = Config.engine.raw_connection()
                cursor = conn.cursor()
                get_all = "select movie_title, gross from red_hat_movies where gross != 0 order by gross desc fetch first 10 rows only;"

                cursor.execute(get_all)
                print("Selecting top ten most popular movies based on how much they grossed.")
                data =  cursor.fetchall()

                print("Top 10 grossest:")
                for row in data:
                        print(
                                "movie_name: ", row[0],
                                "gross: ", row[1]
                        )
        except (Exception, psycopg2.Error) as error :
                print ("Error while fetching data from PostgreSQL", error)
        finally:
                #closing database connection.
                if(conn):
                        cursor.close()
                        conn.close()
                        print("PostgreSQL connection is closed")

def get_top_ten_directors():
        """
        This method returns the top ten directors based on highest grossing and makes sure
        that there are no duplcate directors.
        """
        try:
                conn = Config.engine.raw_connection()
                cursor = conn.cursor()
                get_all = "SELECT * FROM (select distinct on (director_name) director_name, gross from red_hat_movies where gross != 0) AS sub order by gross desc fetch first 10 rows only;"

                cursor.execute(get_all)
                print("Selecting top ten most popular directors based on films that grossed the most.")
                data =  cursor.fetchall()

                print("Top 10 grossest:")
                for row in data:
                        print(
                                "director_name: ", row[0]
                        )
        except (Exception, psycopg2.Error) as error :
                print ("Error while fetching data from PostgreSQL", error)
        finally:
                #closing database connection.
                if(conn):
                        cursor.close()
                        conn.close()
                        print("PostgreSQL connection is closed")