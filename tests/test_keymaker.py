import boringmindmachine as bmm
from unittest import TestCase
from nose.tools import raises
import os, subprocess, json
from .utils import captured_output


"""
Classes to test BoringKeymaker
"""


thisdir = os.path.abspath(os.path.dirname(__file__))


class TestBoringKeymaker(TestCase):
    """
    Test the BoringKeymaker class.
    """
    def test_boringkeymaker(self):
        """
        Running a smoke test for the BoringKeymaker class
        """
        # it really is boring
        bk = bmm.BoringKeymaker()


class TestBoringOAuthKeymaker(TestCase):
    """
    Test the BoringOAuthKeymaker class.
    This focuses on testing the constructors,
    and the API key init mechanisms.
    """
    token_var = 'token'
    secret_var = 'secret'
    keys_dir = "/tmp/tests/shepherd_test_keys/"
    keys_json = "apikeys.json"

    @classmethod
    def setUpClass(self):
        # Create JSON file for JSON key-loading method
        d = {}
        d[self.token_var.lower()] = 'AAAAA'
        d[self.secret_var.lower()] = 'BBBBB'
        self.keypath = os.path.join(self.keys_dir,self.keys_json)
        with open(self.keypath,'w') as f:
            json.dump(d,f)


    def test_boringoauthkeymaker(self):
        """
        Running a smoke test for the BoringOAuthKeymaker class
        """
        bk = bmm.BoringOAuthKeymaker(token=self.token_var,
                                     secret=self.secret_var)


    def test_boringoauthkeymaker_apikeys_env(self):
        """
        Testing ability to create single key using consumer token from environment vars
        """
        bk = bmm.BoringOAuthKeymaker(token=self.token_var,
                                     secret=self.secret_var)

        # Set application API keys
        os.environ[self.token_var.upper()] = 'AAAAA'
        os.environ[self.secret_var.upper()] = 'BBBBB'

        bk.set_apikeys_env()

        self.assertEqual(bk.credentials[self.token_var.lower()], 'AAAAA')
        self.assertEqual(bk.credentials[self.secret_var.lower()],'BBBBB')

        # Clean up
        os.environ[self.token_var.upper()] = ''
        os.environ[self.secret_var.upper()] = ''


    def test_boringoauthkeymaker_apikeys_file(self):
        """
        Testing ability to create single key using consumer token/secret from JSON file
        """
        bk = bmm.BoringOAuthKeymaker(token=self.token_var,
                                     secret=self.secret_var)

        bk.set_apikeys_file(self.keypath)


    def test_boringoauthkeymaker_apikeys_dict(self):
        """
        Testing ability to create single key using consumer token/secret from dictionary
        """
        bk = bmm.BoringOAuthKeymaker(token=self.token_var,
                                     secret=self.secret_var)

        # Set application API keys
        bk.set_apikeys_dict({ 
            self.token_var.lower() : 'AAAAA',
            self.secret_var.lower() : 'BBBBB'
        })


    @classmethod
    def tearDownClass(self):
        # Remove the keys directory we created
        subprocess.call(['rm','-rf',self.keypath])

