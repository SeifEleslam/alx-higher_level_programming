#!/usr/bin/python3
"""Script to get states starts with 'N' from database"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    state_id = Column(Integer, ForeignKey("states.id", ondelete="CASCADE"))

    # Relationship to State class
    state = relationship("State", backref="cities")
