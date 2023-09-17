#!/usr/bin/python3
'''script that deletes all state objects with a name containing the letter a'''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    passwd = quote_plus(argv[2])
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], passwd, argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (session.query(City, State)
              .select_from(City).join(State, City.state_id == State.id)
              .order_by(City.id).all())

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
