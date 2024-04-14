#!/usr/bin/python3
"""
A module to define the Base and State class using sqlalchemy
"""
from sqlalchemy import Integer, Column, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    A class attribute to represent the states table
    """
    __tablename__ = 'states'

    id = Column(
            Integer, Sequence('user_id_seq'), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
