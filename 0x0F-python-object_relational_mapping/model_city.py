#!/usr/bin/python3
'''a python file that contains the class definition of\
 a city and an instance Base = declarative_base()
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class City(Base):
    '''Class definition of a City'''
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
