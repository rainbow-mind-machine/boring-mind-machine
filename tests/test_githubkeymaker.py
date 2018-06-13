import boringmindmachine as bmm
from unittest import TestCase
from nose.tools import raises
import os, subprocess, json
import tempfile
from .utils import captured_output


"""
We need to work out a way to 
actually "make" (test) keys 
without actually making them.

Like, a TestKey class or a 
test flag that when on will call
make_a_key_just_kidding()
"""


class TestGithubKeymaker(TestCase):
    """
    Test the Github Keymaker class.
    """
    keys_dir = tempfile.gettempdir()
    real_tests = False

    @classmethod
    def setUpClass(self):
        """
        Look for CLIENT_ID and CLIENT_SECRET environment variables.
        If we find them, run the real tests.
        """
        try:
            self.id = os.environ['CLIENT_ID']
            self.secret = os.environ['CLIENT_SECRET']
            self.real_tests = True
        except KeyError:
            self.id = ''
            self.secret = ''
            self.real_tests = False


    def test_github_keymaker(self):
        """
        Run a smoke test for the GithubKeymaker class
        """
        gk = bmm.GithubKeymaker()


    def test_github_make_keys_from_strings(self):
        gk = bmm.GithubKeymaker()

        with captured_output() as (out, err):
            gk.make_a_key('dummy','dummy.json',self.keys_dir)


