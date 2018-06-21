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

```plain
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

```plain
$ ls keys/
bot_key1.json
bot_key2.json
bot_key3.json
```

Now we create a custom Shepherd class that extends the
`_create_sheep()` and `_validate_key()` methods,
and use the custom Shepherd class to 

(We illustrate performing basic key validation by
checking for keys with a particular name.)

```python
import boringmindmachine as bmm

class BlueShepherd(bmm.BoringShepherd):

    def _validate_key(self, bot_key, **kwargs):
        """
        Validate a bot key, passed in as a dictionary.
        Sole purpose of this function: raise an exception if there is a problem.
        """
        required_keys = ['key1','key2','key3']
        for key in required_keys:
            if key not in bot_key.keys():
                err = "ERROR: the bot key is missing a required key '%s'."%(key)
                raise Exception(err)

    def _create_sheep(self):
        sheep = self.sheep_class(bot_key)
        self.flock.append(sheep)
```


## Performing Actions

The Shepherd and Sheep use the dispatcher pattern
to call methods. The dispatcher pattern is used to
turn a string (like "tweet") into a function call
(like `tweet()`).

```python
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
    s.perform_parallel_action('pass_gas')
```

### Adding Parameters to Actions

If we wanted to add a parameter with a default value
(for example, the string being printed by `pass_gas()`),
we can use `**kwargs` as follows;

```python
import boringmindmachine as bmm
import time

class FlatulentSheep(bmm.BoringSheep):
    def pass_gas(self,, **kwargs):
        if 'message' in kwargs:
            msg = kwargs['message']
        else:
            msg = 'pfffffft'
        print(msg)
        time.sleep(30)

if __name__=="__name__":
    s = bmm.BoringShepherd(
                keys_dir = "keys/",
                flock_name = "flatulent_flock",
                sheep_class = FlatulentSheep
    )
    s.perform_parallel_action(
            'pass_gas',
            message = 'FFFRRRRRRRRRAAAAAAAPPPPPPP'
    )
```

