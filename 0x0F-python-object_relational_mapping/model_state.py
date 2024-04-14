#!/usr/bin/python3
from sqlalchemy import Integer, Column, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

Base = sqlalchemy.orm.declarative_base()


class State(Base):
    """
    A class attribute to represent the states table
    """
    __tablename__ = 'states'

    id = Column(
            Integer, Sequence('user_id_seq'), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
