#!/usr/bin/python3
"""
    script that prints the State object with the name passed as
    argument from the database hbtn_0e_6_usa
"""


from sqlalchemy import select, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name == argv[4])

    if query.all():
        for instance in query:
            print(f"{instance.id}")
    else:
        print("Not found")
