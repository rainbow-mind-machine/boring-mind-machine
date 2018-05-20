## BoringKeymaker

There are two boring Keymaker classes:

* BoringKeymaker - super boring 
* BoringOAuthKeymaker - takes two arguments, `token` and `secret`, 
    and defines methods to extract these two tokens from JSON files,
    dictionaries, or environment variables.

That's all, folks!

The BoringKeymaker should be used as the base class when building
bot flocks that use non-OAuth authentication measures.

The BoringOAuthKeymaker should be used as the base class in the 
more common case of bot flocks that use OAuth.

