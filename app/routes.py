import requests

from flask import render_template
from app import app
from app.functions.r import *
from app.functions.rw import *

@app.route('/', methods=['GET'])
def index():
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    # data = import_database()
    
=======
=======
    # data = import_database()
    
>>>>>>> eb0dff566bc332881267c6aa2f7b66392a044b11
    data = get_data()
    for key in data.iloc[2].items():
        print(key[0])
    print(data.iloc[2])
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6d40d85... pandas working properly
=======
    # data = import_database()
    
>>>>>>> e846871... created database and connected
=======
>>>>>>> 6d40d85... pandas working properly
=======
    # data = import_database()
    
>>>>>>> e846871... created database and connected
    # print(data.text)
=======
>>>>>>> eb0dff566bc332881267c6aa2f7b66392a044b11
    return render_template('mainpage.html', title='Main')