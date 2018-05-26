from BoringKeymaker import BoringOAuthKeymaker
import os, re, json
import tempfile, subprocess

from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


class GoogleKeymaker(BoringOAuthKeymaker):
    """
    Do the OAuth dance with Github.
    """
    def __init__(self):
        super().__init__('client_id','client_secret')


    def set_apikeys_env(self):
        warn = "WARNING: The GoogleKeymaker cannot accept API keys "
        warn += "passed via environment variables. You must obtain "
        warn += "a JSON file with your API keys. See the "
        warn += "cheeseburger-mind-machine documentation for details."
        warn += "Remove set_apikeys_env() to remove this warning.\n"
        print(warn)


    def set_apikeys_file(self, f_apikeys):
        """
        Set the API keys using an external JSON file.
        Unlike the parent class, we don't parse the 
        key-value pairs ourselves, we pass it straight
        to the OAuth object.
        """
        if( not exists(f_apikeys) ):
            err = "Error: could not find specified API keys file %s"%(f_apikeys)
            raise Exception(err)

        elif( not isfile(f_apikeys) ):
            err = "ERROR: specified API keys file %s is not a file"%(f_apikeys)
            raise Exception(err)

        self.apikeys_file = f_apikeys


    def set_apikeys_dict(self, d_apikeys):
        warn = "WARNING: The GoogleKeymaker cannot accept API keys "
        warn += "passed via dictionary. You must obtain "
        warn += "a JSON file with your API keys. See the "
        warn += "cheeseburger-mind-machine documentation for details."
        warn += "Remove set_apikeys_dict() to remove this warning.\n"
        print(warn)


    # ---
    # Single Key Method:
    # The workhorse.

    def make_a_key( self,
                    name,
                    json_target,
                    keys_out_dir='keys/',
                    interactive=True,
                    **kwargs):
        """
        Public method to make a single key from a single item.

            name :          Label for the bot

            json_target :   The name of the target JSON file in which to
                            save this bot's OAuth key. 
                            (All paths are ignored.)

            keys_out_dir :  Directory in which to place final JSON keys
                            containing OAuth tokens and other bot info

            interactive :   Go through the interactive three-legged OAuth process
                            (only set to False for testing)
        """
        if os.path.isdir(keys_out_dir) is False:
            subprocess.call(['mkdir','-p',keys_out_dir])

        # Here is where we build logic in to make this 
        # behave gracefully.
        # 
        # If we are passed a json_target that is not .json:
        # - if no extension, add a .json extension and use as json target
        # - if extension, replace extension with .json and use as json target
        # 
        # That way, we can use this as a files keymaker too
        # 
        _, ext = os.path.splitext(json_target)
        if(ext == ''):
            json_target = json_target + ".json"
        elif(ext == '.json'):
            pass
        else:
            json_target = re.sub(ext,'.json',json_target)

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
        # Once you say yes, it will download a JSON file
        # which you will need to move to the present
        # directory. 
        #
        # Unfortunately, this cannot be automated 
        # because Google. Fortunately, it's a one
        # time process.

        print(" ~"*40)
        print("IMPORTANT:")
        print("Once you have gone through the Google authentication process,")
        print("you will be asked to download a file.")
        print("")

        print("You must copy the file you download to the following location:")
        print("%s"%(full_json_target))
        print("")
        ui = input("Press enter when you have moved the file.")

        while os.path.isdir(full_json_target) is False:
            print("Unable to find %s, copy the JSON file that you downloaded to %s."%(
                full_json_target,full_json_target))
            print("")
            ui = input("Press enter when you have moved the file.")

        print("\n\nCreated key for %s at %s\n\n"%(name,keyloc))

        ### # Create a new OAuth2Session and test it:
        ### del github
        ### github2 = OAuth2Session(token=final_key['token'], client_id=final_key['client_id'])

        ### # Fetch a protected resource, i.e. user profile
        ### r = github2.get('https://api.github.com/user')
        ### print(r.content)

