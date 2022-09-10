#!/usr/bin/python3
"""Start link class to cities table in database """
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer , Column

Base = declarative_base()

class City(Base):
    __table__ = 'cities'
    id = Column(Integer,primary_key=True,autoincremnet=True,nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)

    def __repr__(self) -> str:
    return super().__repr__()