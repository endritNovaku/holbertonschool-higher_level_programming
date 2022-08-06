#!/usr/bin/python3
"""Module that contain class definition"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """state class"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement="auto",
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
