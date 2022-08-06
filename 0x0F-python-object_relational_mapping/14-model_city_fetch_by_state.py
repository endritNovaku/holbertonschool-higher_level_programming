#!/usr/bin/python3
"""prints all city object from the database"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State, City)\
                    .filter(State.id == City.state_id).order_by(City.id).all()

    for s, c in cities:
        print(f"{s.name}: ({c.id}) {c.name}")
    session.close()
