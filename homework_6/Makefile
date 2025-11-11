.PHONY: compare
compare:
	pytest compare/test_compare.py

.PHONY: iterative
iterative:
	pytest iterative/test_iterative.py

.PHONY: k_th
k_th:
	pytest k_th/test_k_th.py

.PHONY: lint
lint:
	mypy compare/*.py iterative/*.py k_th/*.py
	ruff check compare/*.py iterative/*.py k_th/*.py

.PHONY: format
format:
	ruff format compare/*.py iterative/*.py k_th/*.py