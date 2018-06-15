# Twitter Keymaker Example

See [boring-mind-machine/examples/twitter](https://github.com/rainbow-mind-machine/boring-mind-machine/tree/master/examples/twitter).

An example of creating a Twitter OAuth keymaker.

## Creating a Twitter App

The brief summary of creating a Twitter App.

### Set Up API and Create App

Turn on the API (takes a day?). Create an app using your bot master account.

### Creating/Getting App Credentials

Get consumer token and consumer token secret.

### End Result

End result is you should have two pieces of information,
which you can pass to the program using environment variables
(easiest) or other methods.


## Authorizing

In the authorization step, the Keymaker generates a login link/token
for the user to visit and log in using their account. This then sends
the user back to the application with a token.

The user can provide the application API keys to the Keymaker via file,
environment variable, or dictionary. The Keymaker will use the application
API credentials and will guide the user through the process of authenticating.
This uses Twitter's PIN-based authentication method.

```
$ CONSUMER_TOKEN="..." \
  CONSUMER_TOKEN_SECRET="..." \
  python twitter_auth.py
```

