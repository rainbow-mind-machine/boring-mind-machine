# Google Keymaker Example

An example of creating a Google OAuth keymaker.

## Creating a Google App

See [Setup](Setup.md).

## Authorizing

To perform the authorization step, where the Keymaker generates a login
link for the user and asks for permission to perform actions on behalf
of the Google account, specify the location of the Google OAuth
application's API keys.

```
$ GOOGLE_APPLICATION_CREDENTIALS=${PWD}/client_secret.json \
    python google_auth.py
```

