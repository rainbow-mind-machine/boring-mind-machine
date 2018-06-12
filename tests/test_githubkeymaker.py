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

    @classmethod
    def setUpClass(self):
        """
        Create a key directory.
        (Don't know why - we don't actually make anything anyway...)
        """
        self.keypath = os.path.join(self.keys_dir, self.keys_json)
        subprocess.call(['mkdir','-p',self.keys_dir])


    def test_github_keymaker(self):
        """
        Run a smoke test for the GithubKeymaker class
        """
        gk = bmm.GithubKeymaker()


    def test_github_make_keys_from_strings(self):
        gk = bmm.GithubKeymaker()

        with captured_output() as (out, err):
            make_keys_from_strings(['asdf','qwerty'], 'keys/')






