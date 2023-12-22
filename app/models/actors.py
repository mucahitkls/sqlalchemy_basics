from app.database import Base
from datetime import date
from sqlalchemy import Column, String, Integer, Date


class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birthday = Column(Date)

    def __init__(self, name: str, birthday: date):
        self.name = name
        self.birthday = birthday
