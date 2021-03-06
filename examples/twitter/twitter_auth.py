import boringmindmachine as bmm
import subprocess

"""
Run this example like:
    
    $ python twitter_auth.py

This requires that you set up API keys.
Use consumer_token and consumer_token_secret.
"""

keydir = 'keys'

gk = bmm.TwitterKeymaker()
gk.set_apikeys_file('apikeys.json')

print("Creating a dummy key...")
gk.make_a_key('dummy','dummy.json',keydir)
print("Success.")

print("Cleaning up...")
subprocess.call(['rm','-rf',keydir])
print("Done.")

