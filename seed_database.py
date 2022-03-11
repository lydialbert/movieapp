"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import CRUD
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
for movie in movie_data:
    title = movie["title"]
    overview = movie["overview"]
    poster_path = movie["poster_path"]
   
    release_date = datetime.strptime(movie["release_date"], "%Y-%M-%d")

    title = CRUD.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(title)

model.db.session.add_all(movies_in_db)
model.db.session.commit()

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = f'test{n}'
    user = CRUD.create_user(email, password)
    model.db.session.add(user)

    for r in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1, 5)

        rating = CRUD.create_rating(user, random_movie, score)
        model.db.session.add(rating)

model.db.session.commit()
