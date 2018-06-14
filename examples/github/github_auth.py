import boringmindmachine as bmm
import subprocess

"""
Run this example like:

$ CLIENT_ID="XXXXX" \
  CLIENT_SECRET="XXXXXXXX" \
  python github_auth.py

Where CLIENT_ID and CLIENT_SECRET are 
from your app page on Github.
"""

keydir = 'keys'

gk = bmm.GithubKeymaker()
gk.set_apikeys_env()

print("Creating a dummy key...")
gk.make_a_key('dummy','dummy.json',keydir)
print("Success.")

print("Cleaning up...")
subprocess.call(['rm','-rf',keydir])
print("Done.")

