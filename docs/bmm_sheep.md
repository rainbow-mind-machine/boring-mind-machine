# Boring Sheep

(TODO: Copy Sheep materials over, and copy Shepherd docs)

(TODO: What are the most common ways to extend Sheep? essential methods/call
traces?)

The Sheep is the class that represents a single user account on the
third party service the mind machine is defining. In general, the pattern
that mind machine bot flocks follow is: 1 Sheep = 1 bot account = 1 action.

The `BoringSheep` class is really boring, because we don't want to impose
restrictions or make assumptions by implementing a bunch of functionality.

### How to use the Boring Sheep class? (...don't)

The constructor is where you create the Sheep's API instance, and should be
defined at the package level.

The Boring Sheep class has a virtual constructor, so it cannot be created
directly. You should instead define a new Sheep class that inherits from
Boring Sheep and defines a constructor, which should initialize an API instance.

### How to extend the Boring Sheep class?

See the [`examples/`](/examples) directory.

### What does the Boring Sheep class define?

In addition to mentioning what you have to define,
let's mention what you don't have to define.

The Boring Sheep class implements a dispatcher pattern,
which is a way of passing the name of an action as a
string, and turning that into a function call.

For example, if the user asks for the 'dummy' action
via `sheep.perform_action('dummy',**kwargs)`, this will 
call `sheep.dummy(**kwargs)`.

See [command pattern (wikipedia)](https://en.wikipedia.org/wiki/Command_pattern)
for a detailed description of the dispatcher pattern.

```python
    def perform_action(self,action,**kwargs):
        # Dispatcher pattern
        if hasattr(self, action):
            method = getattr(self, action)
            method(**kwargs)
```

