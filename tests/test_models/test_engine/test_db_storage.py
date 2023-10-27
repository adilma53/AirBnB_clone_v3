#!/usr/bin/python3
from models.engine.db_storage import DBStorage
import os
import unittest

@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") != "db",
    "db_storage"
)

class test_db_storage(unittest.TestCase):
    """docs of test class """
    def test_docs(self):
        """docs of func"""
        self.assertIsNot(DBStorage.__doc__, None)


    """" todo these tests later"""
    def test_get(self):
        """ test get method """
        pass

    def test_count(self):
        """ test count method """
        pass
