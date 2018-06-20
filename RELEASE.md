# Release Process

## Workflow to create a new version

For the prime number version system,
a typical workflow to add new features
to a program generally look like this:

* Start from the stable (master) branch (first stable version will be v2)
* Create a development (dev) branch
* Development occurs on the development branch
	* Start from the development (dev) branch
	* Create a feature (feature-1) branch
	* Development occurs on the feature branch
	* When a working candidate is ready, changes from feature-1
		are merged back into dev
* When a release candidate is ready, a release branch is created (release/v3)
* Fixes to prepare the release candidate are made on the release branch
* When the release candidate is stable, it is merged into stable (master)

## Workflow to distribute a new version

Once the new version is tested, stable, and working,
it is time to distribute the code.

* After merging, a new version is tagged (git tag)
* Tags are pushed to Github, making tags available for download via Github
* After new version is tagged, test installing downloaded tag via setup.py
  method in a virtualenv
* Upload new version to Pypi, test pypi release installation via pip install
  method in a virtualenv
* Bump/update versions and tags on Dockerhub as needed

Create a git tag:

```
git tag v2
git push origin v2
```

Test installing downloaded release from Github:

```
wget https://github.com/rainbow-mind-machine/boring-mind-machine/archive/v2.zip
unzip v2.zip

```





