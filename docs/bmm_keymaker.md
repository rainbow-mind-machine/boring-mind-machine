# Boring Keymaker and Boring OAuth Keymaker

![the keymaker](mind-machine-docs/img/keymaker.jpg)

**the mind machine keymaker. trust it with your keys.**

There are two base Keymaker classes implemented by 
boring mind machine; they are `BoringKeymaker` and
`BoringOAuthKeymaker`.

Technically a Keymaker can inherit from BoringKeymaker
and use any authentication method, but in practice all
Keymakers are OAuth Keymakers.


## Constructing the Keymaker

The generic BoringOAuthKeymaker class requires two bits of information:
an API application token and an API application secret. These have
different names for different services, so when you create a Keymaker,
you need to specify the name of the token and the name of the secret
in the Keymaker constructor:

```python
import boringmindmachine as bmm

# create a dummy oauth keymaker class
class MyKeymaker(bmm.BoringOAuthKeymaker):
    pass

k = MyKeymaker(token='client_token',secret='client_secret')
```

For Github, Google, Twitter, etc. Keymakers, this value is already set.

```python
import boringmindmachine as bmm

ghk = bmm.GithubKeymaker()

gk = bmm.GoogleKeymaker()

tk = bmm.TwitterKeymaker()
```


## Passing API Keys to the Keymaker

The Keymaker must have client API keys to verify that it is in fact
allowed to take actions as the third-party OAuth application.
The API keys consist of a token and a secret that correspond to
the OAuth app created for the third-party service.

(For example, when you create a Github app, the app page will give
a client ID and a client secret at the top of the page.)

This token and secret can be passed three different ways:

* via environment variables
* via a JSON file
* via a Python dictionary

### Using Environment Variables

To set using environment variables:

**`use_env.py`:**

```python
import boringmindmachine as bmm

class MyKeymaker(bmm.BoringOAuthKeymaker):
    pass

k = MyKeymaker(token='client_token',secret='client_secret')
k.set_apikeys_env()
```

This would then look for two environment variables corresponding to
the name of the token and secret in all caps. In the above case,
we would need to run the script and provide the API keys as follows:

```plain
$ CLIENT_TOKEN="abcd" CLIENT_SECRET="qwerty" use_env.py
```

### Using JSON File

To use a JSON file, create a simple JSON file with two key-value pairs.
The two keys should be the token name and the secret name provided to the
constructor. 

**`apikeys.json`:**

```json
{
    "client_token" : "asdf",
    "client_secret" : "qwerty"
}
```

The corresponding call to set the Keymaker API tokens would look like:

**`use_json.py`:**

```python
import boringmindmachine as bmm

class MyKeymaker(bmm.BoringOAuthKeymaker):
    pass

k = MyKeymaker(token='client_token',secret='client_secret')
k.set_apikeys_json('apikeys.json')
```

### Using Python Dict


**`use_dict.py`:**

```python
import boringmindmachine as bmm

class MyKeymaker(bmm.BoringOAuthKeymaker):
    pass

k = MyKeymaker(token='client_token',secret='client_secret')
k.set_apikeys_dict({
            'client_token' : 'asdf',
            'client_secret' : 'qwerty'
})
```


