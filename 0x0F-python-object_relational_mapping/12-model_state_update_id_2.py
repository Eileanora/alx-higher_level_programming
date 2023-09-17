#!/usr/bin/python3
'''script that changes the name of a state in the database'''
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

    session.query(State).filter(State.id == 2).update(
        {State.name: 'New Mexico'}, synchronize_session=False)
    session.commit()
    session.close()
