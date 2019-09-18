## Description

This is a small project for a python position. Given access to a set of data in .csv format, found [here](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset/data), this project imports the data into a local postgreSQL server for manipulation. It is running as a web application using Flask and the importing and data maniplulation is done with the help of SQLAlchemy.

## Dependencies

The dependencies for this project can be found in the file labeled "requirements.txt"

## Running the code

To run the code you have to make sure that you have python installed. I am using a script to write local environment variable for the database url. To connect to your own postgres server you will have to create an environment variable named 'DATABASE_URL'. 

Next create a virtual environment to run the application using: 
```python -m venv venv```
Once that is made you can import all dependencies by running:
```pip install -r reuirements.txt```
All dependencies will be install. This can take some time depending on your pc.

I have included a .flaskenv file that will have the location of the flask app and the environment in which the app is to be ran. At the moment it is default development.

Once all this is done and you have a database url and it is up and running you can type:
```flask run```
to start the application.

To import the database to your postgres server open up you browser and enter this link:[localhost:5000/import_database](localhost:5000/import_database).

The two maain functions that this project current have is to compute the top 10 genres in decreasing order by their profitability, and the top 10  directors in decreasing order by their profitability.

To find the top genres use this link: [localhost:5000/top_ten_movies](localhost:5000/top_ten_movies) and to find the top directors use this one: [localhost:5000/top_ten_directors](localhost:5000/top_ten_directors).

## Some things I would like to add

There is an example html template I used as a placehold to potentially show a table  of  whatever data you want to return. I was working on building more of a REST api but time didn't  allow me to completely finish it. It also utilizes jinja to pass variables to the template. 

I also would like to utilize pandas more to manipulate the data from the csv as it can get all the information that the project was supposed to return without the use of a database, but I focussed on building the database instead this time.

Also building a React or Angular front end off of this Flask backend is super simple to get up and running too.

## Author
Jake Pifer
