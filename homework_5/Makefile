.PHONY: permutations
permutations:
	pytest permutations/test_permutations.py

.PHONY: avl
avl:
	pytest avl/test_avl.py

.PHONY: lint
lint:
	mypy tracer/*.py permutations/*.py avl/*.py
	ruff check tracer/*.py permutations/*.py avl/*.py

.PHONY: format
format:
	ruff format tracer/*.py permutations/*.py avl/*.py