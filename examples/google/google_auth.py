import boringmindmachine as bmm
import subprocess

"""
Run this example like:
    
    $ python google_auth.py

This requires that you set up API keys
using a JSON file, downloaded from the
Google API Credentials page in the
Google Cloud Platform Console.
"""

keydir = 'keys'

gk = bmm.GoogleKeymaker()
gk.set_apikeys_file('client_secret.json')

print("Creating a dummy key...")
gk.make_a_key('dummy','dummy.json',keydir)
print("Success.")

print("Cleaning up...")
subprocess.call(['rm','-rf',keydir])
print("Done.")


