#!/usr/bin/env python3
""" The user module
"""
from SQLAlchemy import Column, Integer, String
from SQLAlchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ A user class for the user table
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __repr__(self):
        """ A string representation of the instances
        """
        return f"User({self.id}, {self.email}, {self.hashed_password}, {self.session_id}, \
                {self.reset_token})"
