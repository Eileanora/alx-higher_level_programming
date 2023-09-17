#!/usr/bin/python3
'''script that deletes all state objects with a name containing the letter a'''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from model_state import Base, State


if __name__ == "__main__":
    passwd = quote_plus(argv[2])
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], passwd, argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()
    session.close()
