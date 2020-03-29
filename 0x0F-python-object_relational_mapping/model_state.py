#!/usr/bin/python3
''' script that def state'''


import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    '''def state'''

    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
