# boring-mind-machine

**boring mind machine** is a set of boring base classes for building awesome bot flocks.

## boring classes

here are all of the boring classes:

* [BoringLumberjack](lumberjack.md)
* [BoringKeymaker](keymaker.md)
* [BoringShepherd](shepherd.md)
* [BoringSheep](sheep.md)

(The BoringLumberjack is so boring, it doesn't count as a class.)

This follows the **mind machine** architecuture:

* Keymaker - takes care of authentication
* Shepherd - constructs each sheep with keys
* Sheep - uses keys to create API instance

**boring mind machine** is not capable of much.
sometimes though, boring means easy to understand.

## developer workflow

This simple repo helps provide a barebones example of tooling and infrastructure.

Tooling woorkflow:

* [Github](dev/github.md) - setup for workflow and project management on github
* [CircleCI](dev/circleci.md) - continuous integration + deployment to pypi with circle ci
* [Pypi](dev/pypi.md) - uploading project to pypi
* [Dockerhub](dev/dockerhub.md) - pushing container to dockerhub

Project infrastructure:

* [Mailing List](dev/mailing.md)
* [Website](dev/website.md)
* [Issues and PRs](dev/issues_prs.md)
* [Contributing](dev/contributing.md)









