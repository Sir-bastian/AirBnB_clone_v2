#!/usr/bin/python3
""" """
import os

from tests.test_models.test_base_model import TestBasemodel
from models.city import City


class TestCity(TestBasemodel):
    """Represents tests for the city model """

    def __init__(self, *args, **kwargs):
        """Initialises the class"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test type of state_id"""
        new = self.value()
        self.assertEqual(
                type(new.state_id),
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_name(self):
        """Tests the type of name """
        new = self.value()
        self.assertEqual(
                type(new.name),
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
