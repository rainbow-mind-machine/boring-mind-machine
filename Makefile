github_pages: site
	rm -rf site/*
	mkdocs build
	cd site
	git add -A .
	git commit -a -m 'Updating gh-pages site'
	git push origin gh-pages
	git push cmr gh-pages
	cd ../

