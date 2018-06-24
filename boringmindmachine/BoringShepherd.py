import glob, os, sys, json
import subprocess

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool 

from .utils import eprint
from .BoringSheep import BoringSheep


"""
BoringShepherd class 


The Shepherd class spins up the flock of Sheep 
and lets them roam free.

The BoringShepherd class leaves the details of creating Sheep
to the user, but still defines some useful methods. 

The constructor calls a method to setup the flock.
The method to setup the flock loops over each key.
For each key, it:
    - validates the key
    - creates a Sheep from the key

There are also two methods to perform actions with the flock:
one for serial and one for parallel.
"""


class BoringShepherd(object):
    """
    The Shepherd should behave the same for each API,
    since all APIs require keys and all keys will go
    in a JSON file. (Even if it is an empty one.)

    To extend BoringShepherd, 
    define the two methods:

        _validate_key(self,bot_key)

        _create_sheep(self,bot_key)
    """
    def __init__(self, 
                 json_keys_dir, 
                 sheep_class = BoringSheep, 
                 **kwargs):
        """
        This constructor will create a Shepherd.

            json_keys_dir:  Directory where Sheep API keys are located

            sheep_class:    Type of Sheep

            kwargs:         Parameters passed on to the Sheep
        """
        # Shepherds have to keep watch over their flock
        self.sheep_class = sheep_class
        self.flock = []
        self.create_flock(json_keys_dir, **kwargs)

    def create_flock(self, json_keys_dir, **kwargs):
        """
        Create a flock of Sheep from a given directory of keys.

        All **kwargs are added to the bot key.

        Note that separating code out into 
        a method like this makes it easier to
        customize the sheep-key initialization
        behavior of the Keymaker.
        """
        # For each key:
        # - validate key
        # - set up sheep with key
        # These methods need to be defined by 
        # the derived class.

        eprint("boring-mind-machine: BoringShepherd: About to initialize Sheep bot")
        eprint("boring-mind-machine: BoringShepherd: Looking for bot keys in %s"%(json_keys_dir))

        if not os.path.exists(json_keys_dir):
            # keys dir does not exist, so make it
            subprocess.call(['mkdir','-p',json_keys_dir])
        elif not os.path.isdir(json_keys_dir):
            err = "ERROR: You have specified a JSON keys directory %s "%(json_keys_dir)
            err += "that is not a directory!"
            raise Exception(err)

        if len(glob.glob(os.path.join(json_keys_dir,'*.json')))==0:
            err = "ERROR: You have specified a JSON keys directory %s "%(json_keys_dir)
            err += "that contains no .json files! Did you run your keymaker?"
            raise Exception(err)

        for json_file in glob.glob(os.path.join(json_keys_dir,'*.json')):
            bot_key = {}
            eprint("boring-mind-machine: BoringShepherd: Found bot key %s"%(json_file))
            try:
                with open(json_file,'r') as f:
                    bot_key = json.load(f)
            except ValueError:
                err = "ERROR: Invalid JSON bot key in %s"%(json_file)
                raise Exception(err)

            # All kwargs should be added to the bot_key
            for kwarg in kwargs:
                if kwarg not in bot_key.keys():
                    bot_key[kwarg] = kwargs[kwarg]

            # This information might be useful to log

            eprint("boring-mind-machine: BoringShepherd: Validating bot key")
            self._validate_key(bot_key, **kwargs)
            eprint("boring-mind-machine: BoringShepherd: Creating sheep")
            self._create_sheep(bot_key, **kwargs)


    def _validate_key(self, bot_key, **kwargs):
        """virtual method"""
        self.virtual_method(bot_key)


    def _create_sheep(self, bot_key, **kwargs):
        """virtual method"""
        self.virtual_method(bot_key)


    def virtual_method(self):
        err = "ERROR: BoringShepherd is a virtual class and should not be used.\n"
        err += "Define a derived class that defines the following methods:\n"
        err += "    _validate_key(self,bot_key,**kwargs)\n"
        err += "    _create_sheep(self,bot_key,**kwargs)\n\n\n"
        raise Exception(err)


    def perform_serial_action(self, action, **kwargs):
        """
        Perform an action with each bot in serial.
        Good for actions like updating profile.
        """
        if len(self.flock)>0:
            for sheep in self.flock:
                sheep.perform_action(action, **kwargs)
        else:
            err = "ERROR: Tried to perform action, but the Shepherd has no Sheep!"
            raise Exception(err)


    def perform_parallel_action(self, action, **kwargs):
        """
        Perform an action with each bot in parallel.
        Good for tweeting, searching, and continuous tasks.
        """
        def do_it(sheep):
            sheep.perform_action(action, **kwargs)

        pool = ThreadPool(len(self.flock))
        results = pool.map(do_it,self.flock)

