install:
	pip install -e .

build:
	python -m build

publish: build
	python3 -m twine upload dist/*