from .BoringKeymaker import BoringOAuthKeymaker
import os, re, json, time
from os.path import \
    isfile, isdir, exists, join, basename, splitext
import tempfile, subprocess
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

"""
This is the least canonical of all the OAuth Keymakers.
"""

class GoogleKeymaker(BoringOAuthKeymaker):
    """
    Do the OAuth dance with Github.
    """
    def __init__(self):
        super().__init__('client_id','client_secret')


    # ---
    # Google will only allow
    # api keys to be set by file.
    def set_apikeys_env(self):
        err = "ERROR: Google Keymaker cannot create "
        err += "API keys from environment variables. "
        err += "Set the name of the API keys file instead, "
        err += "using set_apikeys_file()"
        raise Exception(err)

    def set_apikeys_dict(self):
        err = "ERROR: Google Keymaker cannot create "
        err += "API keys from a Python dictionary. "
        err += "Set the name of the API keys file instead, "
        err += "using set_apikeys_file()"
        raise Exception(err)

    def set_apikeys_file(self, f_apikeys):
        """
        Set the API keys using an external JSON file.
        This stores the file name in self.apikeys_file,
        since Google auth likes to be given a file name.
        """
        token_var = self.token.lower()

        secret_var = self.secret.lower()

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

        self.apikeys_file = f_apikeys


    # ---
    # Single Key Method:
    # The workhorse.

    def make_a_key( self,
                    name,
                    json_target,
                    keys_out_dir='keys/',
                    **kwargs):
        """
        Public method to make a single key from a single item.

            name :          Label for the bot

            json_target :   The name of the target JSON file in which to
                            save this bot's OAuth key. 
                            (All paths are ignored.)

            keys_out_dir :  Directory in which to place final JSON keys
                            containing OAuth tokens and other bot info
        """
        if os.path.isdir(keys_out_dir) is False:
            subprocess.call(['mkdir','-p',keys_out_dir])

        # strip paths from json_target file name
        json_target = os.path.basename(json_target)

        # ------------8<----------------8<--------------
        # Begin Google-Specific Section

        # Setup the Drive v3 API
        # 
        # Give it access to ALL THE THINGS (files plus metadata)
        # 
        # https://developers.google.com/identity/protocols/googlescopes#drivev3
        #
        SCOPES = 'https://www.googleapis.com/auth/drive'

        # Target file (where credentials will go)
        full_json_target = os.path.join(keys_out_dir,json_target)
        store = file.Storage(full_json_target)
        creds = store.get()

        if os.path.exists(full_json_target):
            raise Exception("Key file %s already exists!"%(full_json_target))

        # Start the client flow with the given credentials
        if not creds or creds.invalid:
            # self.token/self.secret
            flow = client.flow_from_clientsecrets(self.apikeys_file, SCOPES)
            creds = tools.run_flow(flow, store)

        service = build('drive', 'v3', http=creds.authorize(Http()))

        # This will open your browser and present you with
        # a login page asking if you will let 
        # cheeseburger mind machine access the 
        # bot account.
        # 
        # When you say yes, it will return the necessary
        # credentials to this process (which is listening).
        # The service will take care of populating the
        # json key.

        count = 0
        while os.path.isfile(full_json_target) is False:
            count += 1
            print("Waiting for auth process to create JSON file %s..."%(
                full_json_target))
            time.sleep(3) 
            if count>10:
                print("No JSON file detected after 30 seconds. Abort!")
                exit(1)

        # Need to add params to json file

        print("\n\nCreated key for %s at %s\n\n"%(name,full_json_target))

        ### # Create a new OAuth2Session and test it:
        ### del github
        ### github2 = OAuth2Session(token=final_key['token'], client_id=final_key['client_id'])

        ### # Fetch a protected resource, i.e. user profile
        ### r = github2.get('https://api.github.com/user')
        ### print(r.content)

