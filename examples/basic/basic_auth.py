import boringmindmachine as bmm
import os, tempfile
import tempfile

token_var = 'token'
secret_var = 'secret'
keys_json = "fake_apikeys.json"
keypath = os.path.join(os.getcwd(),keys_json)

bk = bmm.BoringOAuthKeymaker(token=token_var,
                             secret=secret_var)
bk.set_apikeys_file(keypath)

if(bk.credentials[token_var] == 'AAAAA' and
    bk.credentials[secret_var] == 'BBBBB'):
    print("Successfully created a BoringOAuthKeymaker")


