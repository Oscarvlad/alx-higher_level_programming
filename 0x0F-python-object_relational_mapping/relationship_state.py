#!/usr/bin/python3
"""
    Get the cities of 1 state of a database
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
