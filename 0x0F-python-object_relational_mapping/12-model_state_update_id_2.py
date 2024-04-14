r!/usr/bin/python3
"""
A script to fetch data in the states table using sqlalchemy
"""
from sqlalchemy import create_engine, select, MetaData
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).filter(State.id == '2').first()
    state.name = "New Mexico"
    session.commit()
