.PHONY: graph
graph:
	pytest graph/test_graph.py

.PHONY: dijkstras
dijkstras:
	pytest dijkstras/test_dijkstras.py

.PHONY: k_th
k_th:
	pytest k_th/test_k_th.py

.PHONY: lint
lint:
	mypy graph/*.py dijkstras/*.py k_th/*.py
	ruff check graph/*.py dijkstras/*.py k_th/*.py

.PHONY: format
format:
	ruff format graph/*.py dijkstras/*.py k_th/*.py