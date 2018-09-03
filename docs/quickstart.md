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

From here, the next step is to start creating
derived classes - custom keymakers for various
services like Twitter ([rainbow-mind-machine](https://github.com/rainbow-mind-machine/rainbow-mind-machine))
or Github ([embarcadero-mind-machine](https://github.com/rainbow-mind-machine/embarcadero-mind-machine)),
and to create custom Shepherd or Sheep classes
to set up and run the bot flock.

See the [`examples/`](/examples/) directory for
additional examples.
