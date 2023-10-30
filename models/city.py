#!/usr/bin/python3
"""Module to hold the City class definition."""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """City class to represent cities."""
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship(
            "Place",
            cascade='all, delete, delete-orphan',
            backref="cities"
        )
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a City instance."""
        super().__init__(*args, **kwargs)
