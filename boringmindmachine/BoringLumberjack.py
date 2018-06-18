import logging

"""
Lumberjack is the logger.

Advanced configuration with logging:

    https://docs.python.org/3/library/logging.config.html#logging-config-api

can package up logging configuration dictionaries
as .yaml files, in addition to json, etc.

But that's a little too fancy for our purposes.
"""

class BoringLumberjack(object):
    """
    The Lumberjack class just configures the logs
    and then it's all finished.

    Honestly, we'll almost never need to extend this.
    """

    LOGO = r'''

           B O R I N G 
   
             M I N D
   
               M A C H I N E

   =====================================

                  Don't mind me -
                    I'm the Lumberjack, 
                        configuring your logs.

'''

    def __init__(self, 
                 flock_name,
                 log_file = 'rainbowmindmachine.log',
                 **kwargs):
        """
        Initialize the logging module to log 
        output from bots to a user-specified file.

        By default, this is rainbowmindmachine.log 
        located in the directory in which the bot 
        script is run.

        The user also specifies a name (for the log).
        """

        # These are pretty solid, so hard-code them
        format_str = " ".join(['%(asctime)s', "[" + flock_name + "]", '%(message)s'])
        date_str = '%m-%d-%Y %H:%M:%S'

        # Configure logging
        logging.basicConfig(level = logging.INFO,
                            datefmt = date_str)

        formatter = logging.Formatter(format_str)

        logger = logging.getLogger('rainbowmindmachine')

        if 'filehandler' in kwargs and kwargs['filehandler']==False:
            pass
        else:
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.INFO)
            logger.addHandler(fh)

        logger.info(self.LOGO)
        logger.info("-"*40)
        logger.info("Flock name: %s"%(flock_name))
        logger.info("Flock log file: %s"%(log_file))
        logger.info("-"*40)

