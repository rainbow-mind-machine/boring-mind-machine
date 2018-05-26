from BoringKeymaker import BoringOAuthKeymaker
import os, re, json
import tempfile, subprocess

from github import Github
from requests_oauthlib import OAuth2Session


class GithubKeymaker(BoringOAuthKeymaker):
    """
    Do the OAuth dance with Github.
    """
    def __init__(self):
        super().__init__('client_id','client_secret')


    # ---
    # Make Bot OAuth Keys

    # Bulk Key Methods:
    # These all call the single key method.

    
    def make_keys_from_strings(self, names, keys_out_dir):
        """
        Just pass in a list of strings (bot names),
        and let the Keymaker do the OAuth dance once
        for each bot name. Simple as that.
        """
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
        for name in d.keys():
            bot_name = self.slugify(name)
            json_target = bot_name + ".json"
            make_a_key(bot_name, json_target, keys_out_dir, bot_name=d[bot_name])


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
        # Begin Github-Specific Section

        # NOTE: This assumes you have set up your webapp
        # to have a callback url of `localhost:8000`
        #
        # This is going to get a bit complicated.
        # Here's what we do:
        # 
        # get set up:
        # - create custom handler class to pull out the parameters we need
        # 
        # oauth process
        # - request an oauth URL from github
        # - run an http server with our custom handler and wait
        # - user visits URL and logs in
        # - user is redirected to localhost
        # - custom handler extracts params, shows ok, and dies

        from urllib.parse import urlparse, parse_qsl
        from http.server import HTTPServer, BaseHTTPRequestHandler

        # This is what we're after:
        query_params = []

        # This is where we stash it:
        callback_file = 'callback_token.json'

        # Start with the custom handler class

        class MyHandler(BaseHTTPRequestHandler):
        
            def do_GET(self):
                url = urlparse(self.path)

                # just save the whole chunka text
                tempf = os.path.join(tempfile.gettempdir(),callback_file)
                with open(tempf,'w') as f:
                    print(self.path,file=f)
                
                # send code 200 response
                self.send_response(200)
        
                # send header first
                self.send_header('Content-type','text-html')
                self.end_headers()
        
                # send file content to client
                self.wfile.write(str.encode("<html><body><h1>Success!</h1></body></html>"))
        
                return 

        scope = 'repo'
        github = OAuth2Session(self.credentials[self.token], scope=scope)

        # OAuth endpoints given in the GitHub API documentation
        authorization_base_url = 'https://github.com/login/oauth/authorize'
        token_url = 'https://github.com/login/oauth/access_token'

        # Redirect user to GitHub for authorization
        authorization_url, state = github.authorization_url(authorization_base_url)
        print("\n\nAuthorizing bot %s\n\n"%(name))
        print("Go to the following URL and log in to authorize this application:\n")
        print("  %s\n\n"%(authorization_url))

        # Now run a server with the custom handler
        server_address = ('', 8000)
        httpd = HTTPServer(server_address, MyHandler)
        httpd.handle_request()

        # Allow for an HTTP callback
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
        with open( os.path.join(tempfile.gettempdir(), callback_file), 'r') as f:
            callback_token = f.read()

        BASE = 'http://localhost:8000'
        redirect_response = BASE + callback_token.strip()

        github = OAuth2Session(self.credentials[self.token], state=state)

        # now use the callback token to receive the oauth token
        github.fetch_token(token_url,
                           client_secret = self.credentials[self.secret],
                           verify = False,
                           scope = scope,
                           authorization_response = redirect_response)

        # now the github object owns the token.
        # can we get the oauth key and create our own token json?
        # we will need to regenerate the github object later anyway.

        final_key = {}
        final_key['token'] = github.token
        final_key['client_id'] = github.client_id
        final_key['name'] = name
        final_key['json_target'] = json_target

        keyloc = os.path.join(keys_out_dir,json_target)
        with open(keyloc,'w') as f:
            json.dump(final_key,f)

        print("\n\nCreated key for %s at %s\n\n"%(name,keyloc))

        ### # Create a new OAuth2Session and test it:
        ### del github
        ### github2 = OAuth2Session(token=final_key['token'], client_id=final_key['client_id'])

        ### # Fetch a protected resource, i.e. user profile
        ### r = github2.get('https://api.github.com/user')
        ### print(r.content)

        # End Github-Specific Section
        # ------------8<----------------8<--------------

