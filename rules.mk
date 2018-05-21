LIB=$(NAME)-mind-machine
SHORT=$(NAME)mindmachine
BMM_GH=git@github.com:rainbow-mind-machine/$(LIB).git
BMM_CMR=ssh://git@git.charlesreid1.com:222/bots/$(LIB).git
MKM_CMR=ssh://git@git.charlesreid1.com:222/charlesreid1/mkdocs-material.git

SHELL := /bin/bash

default: 

########################
# documentation groundwork

initialize_ghpages: fix_remotes
	rm -r site && git clone $(BMM_GH) site
	set -x \
		&& cd site/ \
		&& git remote add cmr $(BMM_CMR) \
		&& git checkout --orphan gh-pages \
		&& rm -rf * .gitmodules .gitignore \
		&& echo '<h2>hello world</h2>' > index.html \
		&& git add index.html \
		&& git commit index.html -m 'add init commit on gh-pages branch' \
		&& git push origin gh-pages \
		&& git push cmr gh-pages \
		&& set +x

initialize_docs: fix_remotes site mkdocs_material

mkdocs_material:
	git submodule add $(MKM_CMR) \
		&& git add mkdocs-material .gitmodules \
		&& git commit mkdocs-material .gitmodules -m 'Initializing mkdocs-material submodule' \
		&& git push origin \
		&& wget https://git.charlesreid1.com/docker/pod-charlesreid1/raw/branch/master/mkdocs.yml \
	mkdir docs && cp README.md docs/index.md

site:
	if [ ! -d site ]; then \
		git clone -b gh-pages $(BMM_GH) site \
	fi 
	cd site && git remote add cmr $(BMM_CMR)

fix_remotes: 
	git remote set-url origin $(BMM_GH)
	git remote set-url cmr $(BMM_CMR)

cmr_remote:
	git remote add cmr $(BMM_CMR)

submodule_init:
	git submodule update --init


########################
# deploy documentation

deploy: site
	rm -rf site/*
	mkdocs build
	cd site; git add -A .; git commit -a -m 'Updating gh-pages site'; git push origin gh-pages; git push cmr gh-pages


#######################
# src init

initialize_src:
	mkdir $(SHORT)
	touch $(SHORT)/__init__.py
	git add $(SHORT) \
		&& git commit $(SHORT) -m 'init commit of src' \
		&& git push origin master \
		&& git push cmr master



########################
# testing 1 2 3

test:
	nosetests -v
