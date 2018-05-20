import os, json

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


    ###########################################
    # Load Application (Consumer) API Keys

    def set_apikeys_env(self):
        """
        Set the API keys using environment variables:

            $CONSUMER_TOKEN
            $CONSUMER_TOKEN_SECRET
        """
        if( os.environ['CONSUMER_TOKEN'] and os.environ['CONSUMER_TOKEN_SECRET'] ):
            self.consumer_token = {}
            self.consumer_token['consumer_token'] = os.environ['CONSUMER_TOKEN']
            self.consumer_token['consumer_token_secret'] = os.environ['CONSUMER_TOKEN']
            self.apikeys_set = True
        else:
            raise Exception("Error: environment variables CONSUMER_TOKEN and CONSUMER_TOKEN_SECRET were not set.")


    def set_apikeys_file(self,f_apikeys):
        """
        Set the API keys using an external JSON file
        with the keys:

            consumer_token
            consumer_token_secret
        """
        if( not exists(f_apikeys) ):
            # Nope, no idea
            raise Exception("Error: could not find specified apikeys file %s"%(f_apikeys))

        elif( not isfile(f_apikeys) ):

            # user specified a directory.
            # check if it contains apikeys.json
            f_apikeys = join(f_apikeys,'apikeys.json')
            if( not isfile( f_apikeys ) ):
                raise Exception("Error: could not find specified apikeys file %s"%(f_apikeys))

        try:
            with open(f_apikeys,'r') as f:
                d = json.load(f)
        except (json.errors.JSONDecodeError):
            raise Exception("Error: given file %s is not valid JSON"%(f_apikeys))
        
        self.set_apikeys_dict(d)


    def set_apikeys_dict(self,d_apikeys):
        """
        Set the API keys by passing a dictionary
        with the keys

            consumer_token
            consumer_token_secret
        """
        ct = ['consumer_token','consumer_token_secret']
        try:
            self.consumer_token = {}
            for k in ct:
                self.consumer_token[k] = d_apikeys[k]

            self.apikeys_set = True

        except(NameError, KeyError):
            err = "Error: could not set API keys, invalid keys provided.\n\n"
            err += "Expected: %s\n\n"%(", ".join(ct))
            err += "Received: %s\n\n"%(", ".join(d_apikeys.keys()))
            raise Exception(err)

