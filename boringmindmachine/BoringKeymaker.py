import os, json, glob
from os.path import \
    isfile, isdir, exists, join, basename, splitext



class BoringKeymaker(object):
    """
    We do only what we are meant to do.

    Keymaker should take a set of items and asks the user
    if they would like to create a key from each item.

    This is completely dependent on the API, so much so
    that there is no common functionality that would be
    useful to share across all Keymakers.
    """
    def __init__(self):
        self.apikeys_set = False


class BoringOAuthKeymaker(BoringKeymaker):
    """
    OAuth is a common enough pattern that we define
    a base class with convenience methods for getting
    API credentials three different ways:
    - environment variables
    - JSON file
    - python dictionary

    API key should have token and one secret token.
    The token/secret labels must be specified. For example,
    - token = credentials
    - secret = credentials_secret

    Why consumer? Because the app consumes the API.

    Final API tokens go into self.credentials
    """
    def __init__(self, token, secret):
        super().__init__()
        self.token = token
        self.secret = secret


    ###########################################
    # Load API Key token/secret

    def set_apikeys_env(self):
        """
        Set the API keys using environment variables
        """
        token_var = self.token
        token_var = token_var.lower()

        secret_var = self.secret
        secret_var = secret_var.lower()

        if(os.environ[token_var.upper()] and os.environ[secret_var.upper()]):
            self.credentials = {}
            self.credentials[token_var]        = os.environ[token_var.upper()]
            self.credentials[secret_var] = os.environ[secret_var.upper()]
            self.apikeys_set = True
        else:
            err = "ERROR: environment variables %s and %s were not set."%(
                    token_var, secret_var)
            raise Exception(err)


    def set_apikeys_file(self, f_apikeys):
        """
        Set the API keys using an external JSON file
        """
        token_var = self.token
        token_var = token_var.lower()

        secret_var = self.secret
        secret_var = secret_var.lower()

        if( not exists(f_apikeys) ):
            err = "Error: could not find specified API keys file %s"%(f_apikeys)
            raise Exception(err)

        elif( not isfile(f_apikeys) ):
            err = "ERROR: specified API keys file %s is not a file"%(f_apikeys)
            raise Exception(err)

        try:
            with open(f_apikeys,'r') as f:
                d = json.load(f)
        except ValueError:
            err = "ERROR: given API keys file %s is not valid JSON"%(f_apikeys)
            raise Exception(err)

        self.set_apikeys_dict(d)


    def set_apikeys_dict(self, d_apikeys):
        """
        Set the API keys by passing a dictionary with the keys
        """
        token_var = self.token
        token_var = token_var.lower()

        secret_var = self.secret
        secret_var = secret_var.lower()

        if token_var not in d_apikeys.keys():
            err = "ERROR: key %s not found in user-provided dictionary (key set: %s)"%(
                    token_var, ",".join(d_apikeys.keys()))
            raise Exception(err)

        if secret_var not in d_apikeys.keys():
            err = "ERROR: key %s not found in user-provided dictionary (key set: %s)"%(
                    secret_var, ",".join(d_apikeys.keys()))
            raise Exception(err)

        self.credentials = {}
        self.credentials[token_var] = d_apikeys[token_var]
        self.credentials[secret_var] = d_apikeys[secret_var]
        self.apikeys_set = True

