#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""


from sqlalchemy import select, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.name, City.id, City.name)\
        .join(City, State.id == City.state_id).order_by(City.id)

    for instance in query:
        print(f"{instance[0]}: ({instance[1]}) {instance[2]}")
