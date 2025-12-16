.PHONY: rabin_karp
rabin_karp:
	pytest rabin_karp/test_rabin_karp.py

.PHONY: knuth_morris_pratt
knuth_morris_pratt:
	pytest knuth_morris_pratt/test_knuth_morris_pratt.py

.PHONY: dag
dag:
	pytest dag/test_dag.py

.PHONY: lint
lint:
	mypy rabin_karp/*.py knuth_morris_pratt/*.py dag/*.py
	ruff check rabin_karp/*.py knuth_morris_pratt/*.py dag/*.py

.PHONY: format
format:
	ruff format rabin_karp/*.py knuth_morris_pratt/*.py dag/*.py