<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# from app import app, db
from app import app
# from app.models import Director, Actor, Movie

# @app.shell_context_processor
# def make_shell_context():
#     """
#     creates a shell context that adds the database instance and models to the shell session
#     CTRL-Z to close shell
#     """
#     return {'db': db, 'Director': Director, 'Actor': Actor, 'Movie': Movie}
=======
=======
>>>>>>> 9941e0e... created database framework
from app import app, db
from app.models import Director, Actor, Movie

@app.shell_context_processor
def make_shell_context():
    """
    creates a shell context that adds the database instance and models to the shell session
    CTRL-Z to close shell
    """
<<<<<<< HEAD
    return {'db': db, 'Director': Director, 'Actor': Actor, 'Movie': Movie}
>>>>>>> 9941e0e... created database framework
=======
# from app import app, db
from app import app
# from app.models import Director, Actor, Movie

=======
# from app import app, db
from app import app
# from app.models import Director, Actor, Movie

>>>>>>> e846871... created database and connected
# @app.shell_context_processor
# def make_shell_context():
#     """
#     creates a shell context that adds the database instance and models to the shell session
#     CTRL-Z to close shell
#     """
<<<<<<< HEAD
#     return {'db': db, 'Director': Director, 'Actor': Actor, 'Movie': Movie}
>>>>>>> e846871... created database and connected
=======
    return {'db': db, 'Director': Director, 'Actor': Actor, 'Movie': Movie}
>>>>>>> 9941e0e... created database framework
=======
#     return {'db': db, 'Director': Director, 'Actor': Actor, 'Movie': Movie}
>>>>>>> e846871... created database and connected
