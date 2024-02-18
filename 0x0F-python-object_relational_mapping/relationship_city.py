#!/usr/bin/python3
"""Script to get states starts with 'N' from database"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """City SQL Class"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    state_id = Column(Integer, ForeignKey(
        "states.id"), nullable=False)
