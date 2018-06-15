# Github Keymaker Example

See [boring-mind-machine/examples/github](https://github.com/rainbow-mind-machine/boring-mind-machine/tree/master/examples/github).

An example of creating a Github OAuth keymaker.

## Creating a Github App

The brief summary of what we cover here:

We need to create an application (something that will consume the API
endpoints), and we need to grant the application access to at least one 
Github account.

### Set Up API and Create App

To create an OAuth app as a user, see 
[these detailed instructions](https://developer.github.com/apps/building-oauth-apps/creating-an-oauth-app/)
from Github.

When you create your OAuth app, the one crucial
piece of information is the callback URL. This is
where the magic token is sent once the user logs in
with their Github account.

The Github Keymaker runs a server on localhost port 8000,
so **the callback URL for your OAuth application should be 
set to `http://localhost:8000`**.

### Getting App Credentials

Once you have created your application, the application's
description page will contain the client ID and client secret
needed to use this application to run mind machine bots
using Github.

### End Result

In the end you should have a pair of API keys (a client ID and
a client secret), which you will pass to the keymaker using
one of the three methods provided (via a dictionary, a JSON
file, or environment variables).

To run the Github Keymaker example, you need to pass the API
keys to the keymaker using one of three methods:

1. Using a dictionary
1. Using a JSON file
1. Using environment variables

To use the latter option, you can run the Github Keymaker program
like this:

```
$ CLIENT_ID="..." CLIENT_SECRET="..." python github_auth.py
```


## Authorizing

To run this, you will need your client ID and client secret.
These can be found by logging in as the user that created the
OAuth application you will be using, or that is an admin on the
organization that owns the OAuth account. Go to the settings page
and find the OAuth Applications listing on the left side. The
OAuth application page will list the client ID and client secret
at the top of the page.

Once you have them, set the `CLIENT_ID` and `CLIENT_SECRET` environment
variables when you run the program, like this:

```
$ CLIENT_ID="..." \
  CLIENT_SECRET="..." \
  python github_auth.py
```

This will create an authorization link, which you can log in to with
any Github account. The Keymaker will create bot keys in `keys/`,
and will then clean up and remove the `keys/` directory.


