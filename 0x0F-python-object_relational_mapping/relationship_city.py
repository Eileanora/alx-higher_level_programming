#!/usr/bin/python3
'''redefining the City class in a way that the cities table is linked to the \
State table'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class City(Base):
    '''Class definition of a City'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
