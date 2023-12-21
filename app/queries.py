from datetime import date
from models import *
from database import LocalSession
session = LocalSession()

movies = session.query(Movie).all()

for movie in movies:
    print(f"{movie.title} was released on {movie.release_date}")

movies = session.query(Movie).filter(Movie.release_date > date(2015, 1, 1)).all()

for movie in movies:
    print(f"{movie.title} was released after 2015")


tom_movies = session.query(Movie).join(Actor, Movie.actors).filter(Actor.name == 'Tom Criuse').all()

print('### Tom Criuse movies:')
for movie in tom_movies:
    print(f'Tom Criuse starred in {movie.title}')
print('')

# 7 - get actors that have house in Glendale
glendale_stars = session.query(Actor).join(ContactDetails).filter(ContactDetails.address.ilike('%glendale%')).all()

print('### Actors that live in Glendale:')
for actor in glendale_stars:
    print(f'{actor.name} has a house in Glendale')
print('')
