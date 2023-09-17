#!/usr/bin/python3
'''script that prints the first state object in db'''
from sys import argv
from model_state import Base, states
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    passwd = quote_plus(argv[2])
    engine = create_engine('mysql+mysqldb://{argv[1]}:{passwd}\
                           @localhost/{argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(states).order_by(states.id).first()

    if states:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")
    session.close()
