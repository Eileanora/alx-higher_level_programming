#!/usr/bin/python3
'''a python file that contains the class definition of\
 a State and an instance Base = declarative_base()
'''
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class states(Base):
    '''Class definition of a State'''
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(128), nullable=False)
