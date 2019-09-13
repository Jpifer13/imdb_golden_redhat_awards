
import pandas as pd

def get_data():
        data = pd.read_csv("movie_metadata.csv") 
        return data
