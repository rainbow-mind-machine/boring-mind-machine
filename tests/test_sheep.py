import boringmindmachine as bmm
from unittest import TestCase
from nose.tools import raises
import os, subprocess
from .utils import captured_output


"""
Classes to test BoringSheep
"""


thisdir = os.path.abspath(os.path.dirname(__file__))

class TestBoringSheep(TestCase):
    """
    Test the Sheep class.

    This should be done before testing the Shepherd, 
    to limit what can go wrong.
    """
    @raises(Exception)
    def test_(self):
        """
        Test ability to create single key using consumer token from environment vars
        """
        keymaker = bmm.BoringSheep()


