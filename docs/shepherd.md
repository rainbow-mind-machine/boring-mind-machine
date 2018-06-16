# Boring Shepherd

The Shepherd class spins up the flock of Sheep 
and lets them roam free.

The BoringShepherd class leaves the details of creating Sheep
to the user, but still defines some useful methods. 

The constructor calls a method to setup the flock.
The method to setup the flock loops over each key.

For each key, it:
- validates the key
- creates a Sheep from the key

There are also two methods to perform actions with the flock:
one for serial and one for parallel.

## Constructor

This defines a generic Shepherd constructor that takes the following
parameters:

* `json_keys_dir`: Directory where Sheep API keys are located
* `flock_name`: The name of the bot flock (used to format log messages)
* `sheep_class`: Type of Sheep
* `**kwargs`: Logging parameters passed directly to Lumberjack logger

**Example:**

Suppose we have the following directory structure:

```
$ ls keys/
bot_key1.json
bot_key2.json
bot_key3.json
```

## Constructor Call Order

The call order for the constructor is as follows:

* Shepherd contructor calls `create_flock()` method
* `create_flock()` method loads each key in a directory and calls two methods:
    * Private method `_validate_key()` is called to check the bot key
    * Private method `_create_sheep()` is called to create the Sheep

To extend the BoringShepherd class,
you must extend both the `_create_sheep()`
and `_validate_key()` classes (they are 
undefined/virtual methods in the base class).

**Example:**

Suppose we have the following directory structure:

```
$ ls keys/
bot_key1.json
bot_key2.json
bot_key3.json
```

Now we create a custom Shepherd class that extends the
`_create_sheep()` and `_validate_key()` methods,
and use the custom Shepherd class to 

(We illustrate performing basic key validation by filtering
keys with a particular name.)

```
import boringmindmachine as bmm

class BlueShepherd(bmm.BoringShepherd):
    def _create_sheep(self):
        pass
    def _validate_key(self):
        pass

if __name__=="__main__":
    s = BlueShepherd( a, b, c )
```


## Performing Actions

The Shepherd and Sheep use the dispatcher pattern
to call methods. The dispatcher pattern is used to
turn a string (like "tweet") into a function call
(like `tweet()`).

```
import boringmindmachine as bmm
import time

class FlatulentSheep(bmm.BoringSheep):
    def pass_gas(self):
        print("pfffft")
        time.sleep(30)

if __name__=="__name__":
    s = bmm.BoringShepherd(
                keys_dir = "keys/",
                flock_name = "flatulent_flock",
                sheep_class = FlatulentSheep
    )
```

(TODO: Finish these examples.)
