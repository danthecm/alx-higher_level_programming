#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':
    # Create the engine to the database
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, db_name), pool_pre_ping=True)

    # Create a configured class Session
    Session = sessionmaker(bind=engine)

    # Create a Session object
    session = Session()

    # Query to get all State objects
    state = session.query(State).order_by(State.id).first()

    # Print each State object
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
