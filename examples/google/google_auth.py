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

def usage():
    print('''
        google_auth.py

        This script creates a Google Keymaker using
        boring mind machine. To use this script,
        set the API key file using set_apikeys_file()
    ''')
    exit(1)


def main():
    keydir = 'keys'
    
    gk = bmm.GoogleKeymaker()
    gk.set_apikeys_file('client_secret.json')
    
    print("Creating a dummy key...")
    gk.make_a_key('dummy','dummy.json',keydir)
    print("Success.")
    
    print("Cleaning up...")
    subprocess.call(['rm','-rf',keydir])
    print("Done.")

if __name__=="__main__":
    main()

