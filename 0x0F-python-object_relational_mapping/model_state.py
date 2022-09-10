#!/usr/bin/python3
"""Start link class to table in database """
from enum import auto
import sys
from tkinter import TRUE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer , Column

Base = declarative_base()

class State(Base):
    __table__ = 'State'
    id = Column(Integer,primary_key=True,autoincremnet=True,nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self) -> str:
    return super().__repr__()
