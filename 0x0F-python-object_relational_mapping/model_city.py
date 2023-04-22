#!/usr/bin/python3
"""
A module containing a City class that
inherits from SQLALchemy declerative_base class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    State Class inheriting from SQLAlchemy Base Class
    containing id and name column
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
