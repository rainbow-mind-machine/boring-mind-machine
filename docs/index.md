# boring-mind-machine

**boring mind machine** is a set of boring base classes for building awesome bot flocks.

The main job of **boring mind machine** is to take care of the boring stuff.
Specifically, (1) provide base classes for all other mind machines, and
(2) provide Keymakers for different services (Github, Google, Twitter, etc.).

## boring classes

here are all of the classes implemented in boring mind machine:

* Keymakers:
    * [BoringKeymaker](keymaker.md)
    * [GithubKeymaker](github.md)
    * [GoogleKeymaker](google.md)
    * [TwitterKeymaker](twitter.md)
* [BoringShepherd](shepherd.md)
* [BoringSheep](sheep.md)
* [BoringLumberjack](lumberjack.md)

This follows the **mind machine** architecuture:

* Keymaker - takes care of authentication
* Shepherd - constructs each sheep with keys
* Sheep - uses keys to create API instance

**boring mind machine** is not capable of much.
sometimes though, boring means easy to understand.

## developer workflow

This simple repo helps provide a barebones example of tooling and infrastructure.

Tooling woorkflow:

* [Github](#dev/github.md) - setup for workflow and project management on github
* [CircleCI](#dev/circleci.md) - continuous integration + deployment to pypi with circle ci
* [Pypi](#dev/pypi.md) - uploading project to pypi
* [Dockerhub](#dev/dockerhub.md) - pushing container to dockerhub

Project infrastructure:

* [Mailing List](#dev/mailing.md)
* [Website](#dev/website.md)
* [Issues and PRs](#dev/issues_prs.md)
* [Contributing](#dev/contributing.md)



