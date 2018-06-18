class BoringSheep(object):
    """
    Because Sheep can do anything,
    we don't want to impose restrictions
    by implementing functionality here.

    The constructor is where you create 
    the Sheep's API instance, and should 
    be defined at the package level.
    """
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


    def dummy(self,**kwargs):
        """dummy method"""
        pass

