#!/usr/bin/python3
"""
A module containing a State class that
inherits from SQLALchemy declerative_base class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State Class inheriting from SQLAlchemy Base Class
    containing id and name column
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
