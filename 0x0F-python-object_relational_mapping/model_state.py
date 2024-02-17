#!/usr/bin/python3
"""Script to get states starts with 'N' from database"""

import MySQLdb as db
from sys import argv as args
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State class for Sql"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
