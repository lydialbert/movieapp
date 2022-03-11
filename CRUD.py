"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(
        title=title, 
        overview=overview,
        release_date=release_date, 
        poster_path=poster_path
    )

    return movie

def get_movies():
    """Return all the movies."""
    
    return Movie.query.all()


def get_movie_by_id(movie_id):
    """Return a movie by its ID."""
    
    movie = Movie.query.get(movie_id)

    return movie
    

def get_users():
    """Return all the users."""
    
    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by its ID."""
    
    user = User.query.get(user_id)

    return user


def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(
        user=user, 
        movie=movie, 
        score=score
    )

    return rating


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()



def check_user_login(email, password):
    """Check the user's password."""
    User.query.filter(User.email == email).first()
    correct_password = User.query.filter(User.password == password).first()

    if correct_password == password:


    return correct_password


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
