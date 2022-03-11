"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import CRUD

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def view_homepage():
    """View the Homepage."""

    return render_template('homepage.html')


@app.route('/movies')
def view_movies():
    """View movies."""
    
    movies = CRUD.get_movies()

    return render_template('all_movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show specific details of a movie."""

    movie = CRUD.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)


@app.route('/users')
def view_users():
    """View users."""
    
    users = CRUD.get_users()

    return render_template('all_users.html', users=users)


@app.route('/users/<user_id>')
def show_user(user_id):
    """Show specific details of a user."""

    user = CRUD.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)


@app.route('/createaccount', methods=["POST"])
def create_account():
    """Creates an account for a user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = CRUD.get_user_by_email(email)
    
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = CRUD.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")


    return redirect('/')


@app.route('/login', methods=['POST'])
def login_page():
    """User succesfully logged in."""

    email = request.form.get("email")
    password = request.form.get("password")


    
if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
