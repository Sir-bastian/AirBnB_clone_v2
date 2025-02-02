#!/usr/bin/python3
"""Test module for Review Model"""

import os
from tests.test_models.test_base_model import TestBasemodel
from models.review import Review


class TestReview(TestBasemodel):
    """ Representation for Review model test case"""

    def __init__(self, *args, **kwargs):
        """ Initialises the class"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Tests case for place_id"""
        new = self.value()
        self.assertEqual(
                type(new.place_id),
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)

        )

    def test_user_id(self):
        """User test case """
        new = self.value()
        self.assertEqual(
                type(new.user_id),
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_text(self):
        """Tets for the type of text"""
        new = self.value()
        self.assertEqual(
                type(new.text),
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
