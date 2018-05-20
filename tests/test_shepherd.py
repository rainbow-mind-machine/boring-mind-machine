import boringmindmachine as bmm
from unittest import TestCase
from nose.tools import raises
import sys, os, subprocess, logging, json
from .utils import captured_output, LoggingContext


"""
Test Shepherd classes
"""


thisdir = os.path.abspath(os.path.dirname(__file__))

class TestShepherd(TestCase):
    """
    Test the Shepherd class.
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


    #@raises(Exception)
    def test_boringshepherd(self):
        """
        Create a BoringShepherd.

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
        with open('/tmp/somefile','w') as f:
            f.write(result.decode('utf-8'))
        #bs = bmm.BoringShepherd(json_keys_dir = self.keys_dir,
        #                        name = 'Boring Flock',
        #                        streamhandler = False)


        '''
    def test_lessboringshepherd(self):

        class LessBoringSheep(bmm.BoringSheep):
            def __init__(self):
                pass

        class LessBoringShepherd(bmm.BoringShepherd):
            def _validate_key(self, bot_key):
                pass
            def _create_sheep(self, bot_key):
                pass

        lbs = bmm.BoringShepherd(json_keys_dir = self.keys_dir,
                                 name = 'Boring Flock')
        lbs.perform_serial_action('dummy', foo='bar')
        lbs.perform_parallel_action('dummy', foo='bar')
        '''



###        logger = logging.getLogger('rainbowmindmachine')
###        h = logging.StreamHandler(sys.stdout)
###
###        # this "with" block ensures logs print to stdout
###        with LoggingContext(logger, level=logging.INFO, handler=h, close=True):
###
###            # this "with" block ensures we capture stdout
###            with captured_output() as (out, err):
###
###                # Create the Shepherd (this starts the logger)
###                s = rmm.Shepherd(
###                    flock_name = 'test flock',
###                    json_keys_dir = 'tests/shepherd_test_keys',
###                    sheep_class = rmm.Sheep
###                )
###
###            stderrlog = err.getvalue().strip()
###            self.assertIn('Creating flock', stderrlog)
###            self.assertIn('Successfully created', stderrlog)
###            self.assertEqual('test flock',s.name)


    @classmethod
    def tearDownClass(self):
        """
        Clean up the fake bot keys
        """
        #rmdir_cmd = ['rm', '-rf', self.keys_dir]
        #subprocess.call(rmdir_cmd)

        #rmlog_cmd = ['rm', '-rf', 'rainbowmindmachine.log']
        #subprocess.call(rmlog_cmd)


