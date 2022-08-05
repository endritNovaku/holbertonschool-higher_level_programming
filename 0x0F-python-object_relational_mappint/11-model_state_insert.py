#!/usr/bin/python3
"""add a user"""
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__=="__main__":

