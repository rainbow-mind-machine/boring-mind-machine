from .BoringKeymaker import *
from .BoringShepherd import *
from .BoringSheep import *

import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=log_file,
                    filemode='w')

logging.info('BoringMindMachine __init__: Logging has been set up')
