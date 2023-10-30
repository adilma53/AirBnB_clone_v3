#!/usr/bin/python3
"""This is the user class"""

import models
from models import Place
from models import Review

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

class User(BaseModel, Base):
    """User user model"""

    __tablename__ = "users"
    if storage_type == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", cascade="all, delete" ,backref="user")
        review = relationship("Review", cascade="all, delete" ,backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
