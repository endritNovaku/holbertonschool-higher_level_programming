#!/usr/bin/python3
"""city class"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class City(Base):
    __tablename__='cities'
    id = Column(Integer, autoincrement="auto",
            primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
