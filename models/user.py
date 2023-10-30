#!/usr/bin/python3
"""Module to hold the User class definition."""
import hashlib
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """User class to represent users."""
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(
            "Place",
            cascade="all, delete, delete-orphan",
            backref="user"
        )
        reviews = relationship(
            "Review",
            cascade="all, delete, delete-orphan",
            backref="user"
        )
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a User instance."""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name: str, value) -> None:
        '''Set an attribute of this class to a given value.'''
        if name == 'password':
            if type(value) is str:
                m = hashlib.md5(bytes(value, 'utf-8'))
                super().__setattr__(name, m.hexdigest())
        else:
            super().__setattr__(name, value)
