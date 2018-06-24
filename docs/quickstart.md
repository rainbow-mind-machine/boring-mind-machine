# Quick Start with Boring Mind Machine

Here is a bare minimum example 

```
import boringmindmachine as bmm
import os, tempfile

token_var = 'token'
secret_var = 'secret'
keys_json = "fake_apikeys.json"
keypath = os.path.join(os.getcwd(),keys_json)

bk = bmm.BoringOAuthKeymaker(token=token_var,
                             secret=secret_var)
bk.set_apikeys_file(keypath)
```

See the [`examples/`](/examples/) directory for
additional examples.
