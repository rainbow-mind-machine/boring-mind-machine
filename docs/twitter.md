# Twitter Keymaker Example

See [boring-mind-machine/examples/twitter](https://github.com/rainbow-mind-machine/boring-mind-machine/tree/master/examples/twitter).

An example of creating a Twitter OAuth keymaker.


### Set Up API

(TODO: Instructions on turning on the API and how long it takes.)

## Creating a Twitter App

(TODO: The brief summary of creating a Twitter App.)

## Getting App Credentials

Get consumer token and consumer token secret.

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
$ CONSUMER_TOKEN="..." \
  CONSUMER_TOKEN_SECRET="..." \
  python twitter_auth.py
```

