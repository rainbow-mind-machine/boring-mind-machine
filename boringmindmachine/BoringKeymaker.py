import os, re, json, glob
from os.path import \
    isfile, isdir, exists, join, basename, splitext


class BoringKeymaker(object):
    """
    We do only what we are meant to do.

    Keymaker should take a set of items and asks the user
    if they would like to create a key from each item.

    This is completely dependent on the API, so much so
    that there is not much common functionality that is 
    useful to share across all Keymakers.
    """
    def __init__(self):
        self.apikeys_set = False

    def slugify(self, value):
        """
        Slugify a string (make it safe for filenames and bot names)
        """
        slug = re.sub(r'[^\w-]', '', value).strip().lower()
        return slug 


    # ---
    # Bulk Key Methods:
    # Given a set of items, make one key per item.
    # These all call the single key method (not defined here).

    def make_keys_from_strings(self, names, keys_out_dir):
        """
        Just pass in a list of strings (bot names),
        and let the Keymaker do the OAuth dance once
        for each bot name. Simple as that.
        """
        if not self.apikeys_set:
            err = "ERROR: Could not make bot keys, no API keys set!"
            raise Exception(err)

        for name in names:
            bot_name = self.slugify(name)
            json_target = bot_name + ".json"
            self.make_a_key(name, json_target, keys_out_dir)


    def make_keys_from_dict(self, d, keys_out_dir):
        """
        Pass in a list of key-value pairs, and use the keys 
        as the bot name.
            
            {
                'super_bot' :   '...arbitrary...',
                'spider_bot' :  '...',
                'bat_bot' :     '...'
            }

        The key is the bot name, the value is arbitrary.
        This key-value pair is preserved in the key file.
        """
        if not self.apikeys_set:
            err = "ERROR: Could not make bot keys, no API keys set!"
            raise Exception(err)

        for name in d.keys():
            bot_name = self.slugify(name)
            json_target = bot_name + ".json"
            make_a_key(bot_name, json_target, keys_out_dir, bot_name=d[bot_name])


    def make_a_key(self):
        err = "ERROR: BoringKeymaker does not define a "
        err += "make_a_key() method. Perhaps you created "
        err += "the wrong kind of Sheep.\n"
        raise Exception(err)


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

        try:
            self.credentials = {}
            self.credentials[token_var]        = os.environ[token_var.upper()]
            self.credentials[secret_var] = os.environ[secret_var.upper()]
            self.apikeys_set = True
        except KeyError:
            err = "ERROR: environment variables %s and %s were not set."%(
                    token_var.upper(), secret_var.upper())
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
            err = "ERROR: API token key \"%s\" not found in user-provided dictionary\n"%(token_var)
            err += "API keys file had key set: %s\n"%(
                    ",".join(d_apikeys.keys()))
            err += "API keys file needs key set: %s\n"%(
                    ", ".join([token_var, secret_var]))
            raise Exception(err)

        if secret_var not in d_apikeys.keys():
            err = "ERROR: API secret key \"%s\" not found in user-provided dictionary\n"%(token_var)
            err += "API keys file had key set: %s\n"%(
                    ", ".join(d_apikeys.keys()))
            err += "API keys file needs key set: %s\n"%(
                    ", ".join([token_var, secret_var]))
            raise Exception(err)

        self.credentials = {}
        self.credentials[token_var] = d_apikeys[token_var]
        self.credentials[secret_var] = d_apikeys[secret_var]
        self.apikeys_set = True

