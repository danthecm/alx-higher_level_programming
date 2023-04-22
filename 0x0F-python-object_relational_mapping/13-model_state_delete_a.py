#!/usr/bin/python3
"""
Script that deletes all State objects
that contains the letter a from the a database
"""
import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(username, password, db_name),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)

    for state in query:

        session.delete(state)

    session.commit()

    session.close()
