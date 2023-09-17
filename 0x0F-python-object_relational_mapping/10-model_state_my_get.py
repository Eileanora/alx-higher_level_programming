#!/usr/bin/python3
'''script that prints the state object with name passed as argument'''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from urllib.parse import quote_plus


if __name__ == "__main__":
    passwd = quote_plus(argv[2])
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], passwd, argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == argv[4]).first()

    if states:
        print("{}".format(states.id))
    else:
        print("Not found")
    session.close()
