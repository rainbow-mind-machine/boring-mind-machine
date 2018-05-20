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
    This focuses on testing the constructors,
    and the API key init mechanisms.
    """
    def test_boringkeymaker(self):
        """
        Smoke test for BoringKeymaker
        """
        # it really is boring
        bk = bmm.BoringKeymaker()


class TestBoringOAuthKeymaker(TestCase):
    """
    Test the BoringOAuthKeymaker class.
    This focuses on testing the constructors,
    and the API key init mechanisms.
    """
    ct = 'CONSUMER_TOKEN'
    cts = 'CONSUMER_TOKEN_SECRET'

    @classmethod
    def setUpClass(self):
        self.keys_dir = os.path.join( thisdir, "boringoauthkeymaker_keys" )
        self.api_keys = os.path.join( thisdir, "apikeys.json" )

        d = {}
        d[self.ct.lower()] = 'AAAAA'
        d[self.cts.lower()] = 'BBBBB'
        with open(self.api_keys,'w') as f:
            json.dump(d,f)


    def test_boringoauthkeymaker(self):
        """
        Smoke test for BoringOAuthKeymaker
        """
        # it really is boring
        bk = bmm.BoringOAuthKeymaker()


    def test_boringoauthkeymaker_apikeys_env(self):
        """
        Test ability to create single key using consumer token from environment vars
        """
        keymaker = bmm.BoringOAuthKeymaker()

        # Set application API keys
        os.environ['CONSUMER_TOKEN'] = 'AAAAA'
        os.environ['CONSUMER_TOKEN_SECRET'] = 'BBBBB'

        keymaker.set_apikeys_env()

        # Clean up
        os.environ['CONSUMER_TOKEN'] = ''
        os.environ['CONSUMER_TOKEN_SECRET'] = ''


    def test_boringoauthkeymaker_apikeys_file(self):
        """
        Test ability to create single key using consumer token/secret from JSON file
        """
        keymaker = bmm.BoringOAuthKeymaker()

        # Set application API keys
        apikeys = os.path.join(thisdir,'apikeys.json')

        keymaker.set_apikeys_file(apikeys)


    def test_boringoauthkeymaker_apikeys_dict(self):
        """
        Test ability to create single key using consumer token/secret from dictionary
        """
        keymaker = bmm.BoringOAuthKeymaker()

        # Set application API keys
        keymaker.set_apikeys_dict({ 
            self.ct.lower() : 'AAAAA',
            self.cts.lower() : 'BBBBB'
        })


    @classmethod
    def tearDownClass(self):
        # Remove the keys directory we created
        subprocess.call(['rm','-rf',self.keys_dir])



