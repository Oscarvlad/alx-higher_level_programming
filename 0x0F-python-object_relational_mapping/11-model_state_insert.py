#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""


from sqlalchemy import select, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)

    newObject = State(
            name="Louisiana"
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(newObject)
    session.commit()

    query = session.query(State).order_by(State.id.desc()).first()
    print(query.id)
