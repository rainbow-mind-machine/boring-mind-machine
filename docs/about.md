# About boring mind machine

**boring mind machine (bmm)** is part of the mind machine suite of software,
run by the [rainbow-mind-machine](https://github.com/rainbow-mind-machine)
organization on Github.

Like all mind machines, **boring mind machine** is simple and extensible.


## How is boring mind machine simple?

The **mind machine framework** revolves around providing a few
simple components for building bot flocks:

* [Keymaker classes](mind-machine-docs/keymaker.md)
* [Shepherd classes](mind-machine-docs/shepherd.md)
* [Sheep classes](mind-machine-docs/sheep.md)

But it gets even simpler than that:
[boring-mind-machine](https://pages.charlesreid1.com/boring-mind-machine)
provides a [GithubKeymaker class](https://pages.charlesreid1.com/boring-mind-machine/bmm_keymaker_github/),
so that embarcadero mind machine can focus exclusively on Shepherd and Sheep
classes.

That's pretty simple!


## What does boring mind machine extend or do?

The main job of **boring mind machine** is to take care of the boring stuff.
That means two things:

1. Setting up boring base classes that are designed to be extended by
    all of the other mind machine libraries; and
2. Providing working OAuth Keymakers for every third-party service provider
    that has its own mind machine library. (Github, Google, Twitter, etc.)


### Base classes

Because **boring mind machine** provides base classes, that means it does not extend
classes - it provides the base classes that are extended.

That makes **boring mind machine** unique among the mind machines - every mind
machine library imports boring mind machine no matter what, and every Keymaker
is defined in boring mind machine.

### OAuth Keymakers

The second, most important functionality implemented in bmm are the Keymaker
classes. bmm implements a Keymaker for each service that has a corresponding
mind machine library.

Collecting each Keymaker together makes the logic more clear. Each third party
service implements the same authentication process (OAuth) but everybody does it
differently, so there are many tedious, boring details to work out.

Hence, the "boring".


## How is boring mind machine POOP-y?

Libraries that implement good practices in POOP (Python Object Oriented
Programming) are said to be POOP-y. What makes the boring mind machine library
particularly POOP-y is the fact that it provides the solid foundation on which
the entire mind machine enterprise is constructed.

It is critical that the boring mind machine library be an exemplar of good
practices for software built using the mind machine framework!

