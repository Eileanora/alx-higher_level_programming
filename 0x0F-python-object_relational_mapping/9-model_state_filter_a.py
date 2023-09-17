#!/usr/bin/python3
'''script that lists all state objects that contains letter a'''
from sys import argv
from model_state import Base, states
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


if __name__ == "__main__":
    passwd = quote_plus(argv[2])
    engine = create_engine('mysql+mysqldb://{argv[1]}:{passwd}\
        @localhost/{argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (session.query(states)
              .filter(states.name.like('%a%'))
              .order_by(states.id).all())

    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
