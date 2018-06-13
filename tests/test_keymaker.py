import boringmindmachine as bmm
from unittest import TestCase
from nose.tools import raises
import os, subprocess, json
import tempfile
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

    def test_slugify(self):
        """
        Running a test of the slugify function
        """
        bk = bmm.BoringKeymaker()
        self.assertEquals("a-s-df",bk.slugify("a-?s-$!d(f"))


class TestBoringOAuthKeymaker(TestCase):
    """
    Test the BoringOAuthKeymaker class.
    This focuses on testing the constructors,
    and the API key init mechanisms.
    """
    token_var = 'token'
    secret_var = 'secret'
    keys_dir = tempfile.gettempdir()
    keys_json = "fake_apikeys.json"

    @classmethod
    def setUpClass(self):
        """
        Set up JSON file for JSON key-loading method
        """
        self.keypath = os.path.join(self.keys_dir, self.keys_json)
        subprocess.call(['mkdir','-p',self.keys_dir])

        d = {}

        self.token_var = self.token_var.lower()
        self.secret_var = self.secret_var.lower()

        d[self.token_var] = 'AAAAA'
        d[self.secret_var] = 'BBBBB'

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
        os.environ[self.token_var.upper()] = 'CCCCC'
        os.environ[self.secret_var.upper()] = 'DDDDD'

        bk.set_apikeys_env()

        self.assertEqual(bk.credentials[self.token_var], 'CCCCC')
        self.assertEqual(bk.credentials[self.secret_var],'DDDDD')

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

        # Note that we hard-code these key values in the setup method above...
        self.assertEqual(bk.credentials[self.token_var], 'AAAAA')
        self.assertEqual(bk.credentials[self.secret_var],'BBBBB')


    def test_boringoauthkeymaker_apikeys_dict(self):
        """
        Testing ability to create single key using consumer token/secret from dictionary
        """
        bk = bmm.BoringOAuthKeymaker(token=self.token_var,
                                     secret=self.secret_var)

        # Set application API keys
        bk.set_apikeys_dict({ 
            self.token_var : 'EEEEE',
            self.secret_var : 'FFFFF'
        })

        self.assertEqual(bk.credentials[self.token_var], 'EEEEE')
        self.assertEqual(bk.credentials[self.secret_var],'FFFFF')


    @classmethod
    def tearDownClass(self):
        # Remove the keys directory we created
        subprocess.call(['rm','-rf',self.keypath])

