import os, json
from os.path import \
    isfile, isdir, exists, join, basename, splitext



class BoringKeymaker(object):
    """
    We do only what we are meant to do.

    Keymaker should take a set of items and asks the user
    if they would like to create a key from each item.

    BoringKeymaker, however, only implements functionality 
    to get the app API keys from the user, via
    environment variables, JSON file, or dictionary.
    """
    def __init__(self):
        # We won't do much here
        self.request_token_url = 'https://api.twitter.com/oauth/request_token'
        self.authorize_url = 'https://api.twitter.com/oauth/authorize'
        self.access_token_url = 'https://api.twitter.com/oauth/access_token'
        self.apikeys_set = False



class BoringOAuthKeymaker(BoringKeymaker):
    """
    OAuth is a common enough pattern that we define
    a base class with convenience methods for getting
    OAuth credentials three different ways:
    - environment variables
    - JSON file
    - python dictionary

    By default we expect CONSUMER_TOKEN and CONSUMER_TOKEN_SECRET
    but these can be customized.

    This puts the consumer (app) token in self.consumer_token

    (Why consumer? It consumes the API)
    """
    
    ct = "consumer_token"
    cts = "consumer_token_secret"

    ###########################################
    # Load Application (Consumer) API Keys

    def set_apikeys_env(self, 
                        consumer_token_variable = ct,
                        consumer_token_secret_variable = cts):
        """
        Set the API keys using environment variables
        """
        consumer_token_variable = consumer_token_variable.lower()
        consumer_token_secret_variable = consumer_token_secret_variable.lower()

        if(os.environ[consumer_token_variable.upper()] and os.environ[consumer_token_secret_variable.upper()]):
            self.consumer_token = {}
            self.consumer_token[consumer_token_variable]        = os.environ[consumer_token_variable.upper()]
            self.consumer_token[consumer_token_secret_variable] = os.environ[consumer_token_secret_variable.upper()]
            self.apikeys_set = True
        else:
            err = "ERROR: environment variables %s and %s were not set."%(
                    consumer_token_variable, consumer_token_secret_variable)
            raise Exception(err)


    def set_apikeys_file(self, 
                         f_apikeys, 
                         consumer_token_variable = ct,
                         consumer_token_secret_variable = cts):
        """
        Set the API keys using an external JSON file
        with the keys:

            consumer_token
            consumer_token_secret
        """
        if( not exists(f_apikeys) ):
            err = "Error: could not find specified API keys file %s"%(f_apikeys)
            raise Exception(err)

        elif( not isfile(f_apikeys) ):

            # user specified a directory.
            # check if it contains apikeys.json
            f_apikeys = join(f_apikeys,'apikeys.json')
            if( not isfile( f_apikeys ) ):
                err = "ERROR: could not find specified API keys file %s"%(f_apikeys)
                raise Exception(err)

        try:
            with open(f_apikeys,'r') as f:
                d = json.load(f)
        except (json.errors.JSONDecodeError):
            err = "ERROR: given API keys file %s is not valid JSON"%(f_apikeys)
            raise Exception(err)

        self.set_apikeys_dict(  d, 
                                consumer_token_variable, 
                                consumer_token_secret_variable)


    def set_apikeys_dict(self,
                         d_apikeys,
                         consumer_token_variable = ct,
                         consumer_token_secret_variable = cts):
        """
        Set the API keys by passing a dictionary with the keys
        """
        consumer_token_variable = consumer_token_variable.lower()
        consumer_token_secret_variable = consumer_token_secret_variable.lower()

        if consumer_token_variable not in d_apikeys.keys():
            err = "ERROR: key %s not found in user-provided dictionary (key set: %s)"%(
                    consumer_token_variable, ",".join(d_apikeys.keys()))
            raise Exception(err)

        if consumer_token_secret_variable not in d_apikeys.keys():
            err = "ERROR: key %s not found in user-provided dictionary (key set: %s)"%(
                    consumer_token_secret_variable, ",".join(d_apikeys.keys()))
            raise Exception(err)

        self.consumer_token = {}
        self.consumer_token[consumer_token_variable] = d_apikeys[consumer_token_variable]
        self.consumer_token[consumer_token_secret_variable] = d_apikeys[consumer_token_secret_variable]
        self.apikeys_set = True


