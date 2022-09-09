#!/usr/bin/python3
"""
    Add a state and a city of database
"""
import sys
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_state.cities = [City(name='San Francisco')]
    session.add(new_state)
    session.commit()
