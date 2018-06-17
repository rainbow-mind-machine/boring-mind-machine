# Twitter Keymaker Example

See [boring-mind-machine/examples/twitter](https://github.com/rainbow-mind-machine/boring-mind-machine/tree/master/examples/twitter).

An example of creating a Twitter OAuth keymaker.

## Creating a Twitter App

The brief summary of what we cover here:

We need to create an application (something that will consume the API
endpoints), and we need to grant the application access to at least one 
Twitter account.

### Set Up API

See [Digital Ocean instructions on creating a Twitter app](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app).

## Creating a Twitter App

See [Digital Ocean instructions on creating a Twitter app](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app).

## Getting App Credentials

Get the consumer token and consumer token secret from your application page.

End result is you should have two pieces of information,
which you can pass to the program using environment variables
(easiest) or other methods.

## Authorizing

In the authorization step, the TwitterKeymaker generates a login link/token for
the user to visit and log in using their account. This then sends the user back
to the application with a token.

The user can provide the application API keys to the Keymaker via file,
environment variable, or dictionary. The TwitterKeymaker will use the
application API credentials and will guide the user through the process of
authenticating.  This uses Twitter's PIN-based authentication method.

```
$ python twitter_auth.py
```

### Example Code

**`twitter_auth.py`:**

```python
import boringmindmachine as bmm
import subprocess

keydir = 'keys'

gk = bmm.TwitterKeymaker()
gk.set_apikeys_file('apikeys.json')

# make the Twitter key
print("Creating a dummy key...")
gk.make_a_key('dummy','dummy.json',keydir)
print("Success.")

# Clean up the key
# (remove this bit to keep the key around)
print("Cleaning up...")
subprocess.call(['rm','-rf',keydir])
print("Done.")
```

