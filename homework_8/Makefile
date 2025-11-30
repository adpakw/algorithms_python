.PHONY: graph
graph:
	pytest graph/test_graph.py

.PHONY: dijkstras
dijkstras:
	pytest dijkstras/test_dijkstras.py

.PHONY: dag
dag:
	pytest dag/test_dag.py

.PHONY: lint
lint:
	mypy graph/*.py dijkstras/*.py dag/*.py
	ruff check graph/*.py dijkstras/*.py dag/*.py

.PHONY: format
format:
	ruff format graph/*.py dijkstras/*.py dag/*.py