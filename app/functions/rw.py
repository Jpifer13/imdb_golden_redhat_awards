import csv
import pandas as pd
from app.models import Director, Actor, Movie

def import_database():
    # data = pd.read_csv("movie_metadata.csv") 
    # for key in data.iloc[2].items():
    #     print(key[1])
    # print(data.iloc[2])
    # try:
    #     data.to_sql(con=db, index_label='id', name=golden_db, if_exists='replace')
    # except:
    #     print("didnt work")

    with open('movie_metadata.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row)
            print(row[0])
            print(row[0],row[1],row[2])


