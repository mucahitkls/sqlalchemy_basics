from app.database import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref


class Stuntman(Base):

    __tablename__ = 'stuntmen'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    active = Column(Boolean)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship('Actor', backref=backref('stuntman', uselist=False))

    def __init__(self, name: str, active: Boolean, actor):
        self.name = name
        self.active = active
        self.actor = actor
