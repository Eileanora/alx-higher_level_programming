#!/usr/bin/python3
'''a script that lists all State objects from the database hbtn_0e_6_usa'''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # create engine
    password = quote_plus(argv[2])
    engine = create_engine('mysql+mysqldb://{argv[1]}:{password}\
                           @localhost/{argv[3]}', pool_pre_ping=True)

    # generate database (if not exist)
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()

    # print
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
