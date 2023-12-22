from app.database import Base
from datetime import date
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

movies_actors_association = Table(
    'movies_actors', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    release_date = Column(Date)
    actors = relationship('Actor', secondary=movies_actors_association)

    def __init__(self, title: str, release_date: date):
        self.title = title
        self.release_date = release_date
