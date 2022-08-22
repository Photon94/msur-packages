
build:
	python -m build

clear:
	rm -rf ./dist; rm -rf msur_packages.egg-info

upload:
	twine upload dist/*
