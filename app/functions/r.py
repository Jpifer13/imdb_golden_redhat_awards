import pandas as pd

def get_data_pandas():
        # data = pd.read_csv("movie_metadata.csv", usecols=[9]) 
        data = pd.read_csv("movie_metadata.csv") 
        return data

def get_data_db():
        return 'placeholder'
