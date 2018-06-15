# Twitter Keymaker Example

An example of creating a Twitter OAuth keymaker.

## Creating a Twitter App

See [Setup](Setup.md).

## Authorizing

In the authorization step, the Keymaker generates a login link/token
for the user to visit and log in using their account. This then sends
the user back to the application with a token.

The user can provide the application API keys to the Keymaker via file,
environment variable, or dictionary. The Keymaker will use the application
API credentials and will guide the user through the process of authenticating.
This uses Twitter's PIN-based authentication method.

```
$ python twitter_auth.py
```

