# basic example

A simple example of creating an OAuth keymaker.

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
CLIENT_ID="..." CLIENT_SECRET="..." python basic_auth.py
```

This will create an authorization link, which you can log in to with
any Github account. The Keymaker will create bot keys in `keys/`,
and will then clean up and remove the `keys/` directory.

