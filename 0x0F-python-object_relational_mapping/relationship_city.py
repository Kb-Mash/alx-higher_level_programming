#!/usr/bin/python3

""class definition of a City"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base
from sys import argv


class City(Base):
    """
    Represents a city for a MySQL database.
    Attr:
        id (sqlalchemy.Column): The city's id.
        name (sqlalchemy.Column): The city's name.
        state_id (sqlalchemy.Column): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", foreign_keys=state_id)
