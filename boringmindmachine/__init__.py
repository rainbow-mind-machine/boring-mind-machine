from .BoringKeymaker import *
from .BoringShepherd import *
from .BoringSheep import *

import logging
import os
from datetime import datetime

LOGDIR = '/tmp/mind-machine/'

unique = datetime.now().strftime("%Y%M%d_%H%m%S")
log_filename = "mindmachine_%s.log"%(unique)
log_file = os.path.join(LOGDIR,log_filename)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=log_file,
                    filemode='w')

logging.info('BoringMindMachine: package init: Logging has been set up')
