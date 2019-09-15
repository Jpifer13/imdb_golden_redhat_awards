
import pandas as pd

def get_data():
        # data = pd.read_csv("movie_metadata.csv", usecols=[9]) 
        data = pd.read_csv("movie_metadata.csv") 
        return data
