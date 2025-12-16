.PHONY: rabin_karp
rabin_karp:
	pytest rabin_karp/test_rabin_karp.py

.PHONY: dijkstras
dijkstras:
	pytest dijkstras/test_dijkstras.py

.PHONY: dag
dag:
	pytest dag/test_dag.py

.PHONY: lint
lint:
	mypy rabin_karp/*.py dijkstras/*.py dag/*.py
	ruff check rabin_karp/*.py dijkstras/*.py dag/*.py

.PHONY: format
format:
	ruff format rabin_karp/*.py dijkstras/*.py dag/*.py