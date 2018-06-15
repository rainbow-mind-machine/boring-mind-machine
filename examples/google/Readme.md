# Google Keymaker Example

An example of creating a Google OAuth keymaker.

## Creating a Google App

See [Setup](Setup.md).

## Authorizing

In the authorization step the Keymaker generates a login link/token
for the user to visit and log in with their Google account. The user
is then redirected back to the application with a token that can be
used to perform actions on behalf of the account.

Google requires the application's API keys to be provided via
a JSON file on disk.

To run the Google Keymaker example, specify the API key name in the
`google_auth.py` script (`client_secret.json` by default):

```
$ python google_auth.py
```

