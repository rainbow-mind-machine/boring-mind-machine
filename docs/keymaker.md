# Keymakers

## Base (Boring) Keymaker Classes

There are two base (boring) Keymaker classes:

* BoringKeymaker - super boring 
* BoringOAuthKeymaker - takes two arguments, `token` and `secret`, 
    and defines methods to extract these two tokens from JSON files,
    dictionaries, or environment variables.

The BoringKeymaker should be used as the base class when building
bot flocks that use non-OAuth authentication measures.

The BoringOAuthKeymaker should be used as the base class in the 
more common case of bot flocks that use OAuth.


## Specialty Keymaker Classes

Services like Github, Google, and Twitter have their own Keymakers
to guide the user through the process of authentication with each
service. Current services implemented are:

* [GithubKeymaker](github.md) - used by embarcadero-mind-machine
* [GoogleKeymaker](google.md) - used by cheeseburger-mind-machine (drive), papyrus-mind-machine
  (docs), and waxing-gibbous-mind-machine (calendar)
* [TwitterKeymaker](twitter.md) - used by rainbow-mind-machine

See the [`examples/`](https://github.com/rainbow-mind-machine/boring-mind-machine/tree/master/examples)
directory for examples using each service.


