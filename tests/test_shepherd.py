import boringmindmachine as bmm
from unittest import TestCase
from nose.tools import raises
import sys, os, subprocess, logging, json
from .utils import captured_output, LoggingContext


"""
Test Shepherd classes
"""


thisdir = os.path.abspath(os.path.dirname(__file__))

class TestBoringShepherd(TestCase):
    """
    Test the BoringShepherd class.

    BoringShepherd is a virtual class,
    so we should verify it can't be used,
    then define our own version.
    """
    keys_dir = "/tmp/tests/shepherd_test_keys/"

    @classmethod
    def setUpClass(self):
        """
        Create fake bot keys to simulate the output of the Keymaker. 
        """
        # Create two fake bot keys for two bots
        # 
        fake_bot_keys = [{
            'consumer_token' : 'AAAAA',
            'consumer_token_secret' : 'BBBBB',
            'oauth_token' : 'CCCCC',
            'oauth_token_secret' : 'DDDDD',
            'user_id' : '00000000',
            'screen_name' : 'EEEEE',
            'name' : 'FFFFF',
            'json' : 'bot1.json'
        },
        {
            'consumer_token' : 'ZZZZZ',
            'consumer_token_secret' : 'YYYYY',
            'oauth_token' : 'XXXXX',
            'oauth_token_secret' : 'WWWWW',
            'user_id' : '00000000',
            'screen_name' : 'VVVVV',
            'name' : 'UUUUU',
            'json' : 'bot2.json'
        }]

        mkdir_cmd = ['mkdir', '-p', self.keys_dir]
        subprocess.call(mkdir_cmd)

        for bot_key in fake_bot_keys:
            with open(os.path.join(self.keys_dir,bot_key['json']),'w') as f:
                json.dump(bot_key, f)


    @raises(Exception)
    def test_boringshepherd(self):
        """
        Verifying that BoringShepherd is a virtual class that cannot be used directly.

        Test Notes:
        -------------

        The BoringShepherd expects keys to exist already (that's the Keymaker's job).
        It will create one Sheep per key.

        The BoringShepherd constructor requires:
        - flock name
        - directory containing JSON keys 
        - class of Sheep to use in the flock

        The BoringShepherd calls the virtual methods:
        - _validate_key(self, bot_key)
        - _create_sheep(self, bot_key)

        These must be defined in derived classes, 
        or an exception will be raised. 

        bot_key is the contents of the key JSON file.
        """
        # This should raise an Exception
        result, _ = subprocess.Popen(['ls',self.keys_dir], stdout=subprocess.PIPE).communicate()
        bs = bmm.BoringShepherd(json_keys_dir = self.keys_dir,
                                name = 'Boring Flock',
                                streamhandler = False)



    def test_lessboringshepherd(self):
        """
        Testing functionality of BoringShepherd via derived class LessBoringShepherd
        """

        class LessBoringSheep(bmm.BoringSheep):
            def __init__(self, key):
                self.key = key

        class LessBoringShepherd(bmm.BoringShepherd):
            def _validate_key(self, bot_key):
                pass
            def _create_sheep(self, bot_key):
                self.flock.append(LessBoringSheep(bot_key))

        lbs = LessBoringShepherd(json_keys_dir = self.keys_dir,
                                 name = 'Less Boring Flock',
                                 sheep = LessBoringSheep,
                                 streamhandler = False)
        lbs.perform_serial_action('dummy', foo='bar')
        lbs.perform_parallel_action('dummy', foo='bar')



    @classmethod
    def tearDownClass(self):
        """
        Clean up the fake bot keys
        """
        #rmdir_cmd = ['rm', '-rf', self.keys_dir]
        #subprocess.call(rmdir_cmd)

        #rmlog_cmd = ['rm', '-rf', 'rainbowmindmachine.log']
        #subprocess.call(rmlog_cmd)


