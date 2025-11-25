.PHONY: graph
graph:
	pytest graph/test_graph.py

.PHONY: iterative
iterative:
	pytest iterative/test_iterative.py

.PHONY: k_th
k_th:
	pytest k_th/test_k_th.py

.PHONY: lint
lint:
	mypy graph/*.py iterative/*.py k_th/*.py
	ruff check graph/*.py iterative/*.py k_th/*.py

.PHONY: format
format:
	ruff format graph/*.py iterative/*.py k_th/*.py