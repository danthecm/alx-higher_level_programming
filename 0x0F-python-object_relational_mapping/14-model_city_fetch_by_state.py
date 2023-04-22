#!/usr/bin/python3
"""
A Script that list all the City objects in a database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    uname, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(uname, pwd, db))

    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()

    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
