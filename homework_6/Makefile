.PHONY: compare
compare:
	pytest compare/test_compare.py

.PHONY: iterative
iterative:
	pytest iterative/test_iterative.py

.PHONY: lint
lint:
	mypy compare/*.py iterative/*.py
	ruff check compare/*.py iterative/*.py

.PHONY: format
format:
	ruff format compare/*.py iterative/*.py