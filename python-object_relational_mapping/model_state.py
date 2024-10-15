#!/usr/bin/python3
""" file that contains the class definition of a
State and an instance Base = declarative_base() """
from sqlalchemy import Column, Integer, String
from sqlalchemy import declaritive_base


class State(Base):
	""" state class """
	__tablename__ = 'states'

	id = Column(Integer, primary_key=True, nullable=False)
	Name = Column(String(128), nullable=False)

Base = declarative_base()
