import threading

class BoringSheep(object):
    """
    Because Sheep can do anything,
    we don't want to impose restrictions
    by implementing functionality here.

    This mainly implements a way for Sheep
    (threads) to print messages without
    stepping all over each other.

    The constructor is where you create 
    the Sheep's API instance, and should 
    be defined at the package level.
    """

    # Keep bots from writing over each other:
    # use this lock, and use self.tprint(msg)
    print_lock = threading.Lock()

    def __init__(self):
        err = "ERROR: Sheep constructor initializes API instances "
        err += "and should therefore be defined by the derived class."
        raise Exception(Err)

    def perform_action(self,action,**kwargs):
        """
        The only thing the BoringSheep defines is 
        a perform_action method implementing a
        dispatcher pattern to perform actions.
        
        For example, if the user asks for the 
        'dummy' action, this will look for a 
        self.dummy() method.
        """
        # Dispatcher
        if hasattr(self, action):
            method = getattr(self, action)
            method(**kwargs)
        else:
            err = "Sheep could not figure out how to perform action '{action}'"
            err = err.format(action=action)
            raise Exception(err)

    def tprint(self,*args):
        with self.print_lock:
            print(*args)

    def dummy(self,**kwargs):
        """dummy method"""
        pass

