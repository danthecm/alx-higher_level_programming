#!/usr/bin/python3
"""
Update States where state id is 2 in a database
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query.filter(State.id == 2).first()

    if state:

        state.name = "New Mexico"

        session.commit()

    session.close()
