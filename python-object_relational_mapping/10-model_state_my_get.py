#!/usr/bin/python3
"""  lists all State objects from the database hbtn_0e_6_usa """
import sys
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()
    if state is None:
        print("Nothing")	
    else:
        print(state.id, state.name, sep=": ")
    session.close()
