BMM_GH="git@github.com:rainbow-mind-machine/boring-mind-machine.git"
BMM_CMR="ssh://git@git.charlesreid1.com:222/bots/boring-mind-machine.git"

deploy: site
	rm -rf site/*
	mkdocs build
	cd site; git add -A .; git commit -a -m 'Updating gh-pages site'; git push origin gh-pages; git push cmr gh-pages

site:
	git clone -b gh-pages $(BMM_GH) site
	cd site; git remote add cmr $(BMM_CMR)
