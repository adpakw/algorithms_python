.PHONY: rabin_karp
rabin_karp:
	pytest rabin_karp/test_rabin_karp.py

.PHONY: knuth_morris_pratt
knuth_morris_pratt:
	pytest knuth_morris_pratt/test_knuth_morris_pratt.py

.PHONY: lcs
lcs:
	pytest lcs/test_lcs.py

.PHONY: lint
lint:
	mypy rabin_karp/*.py knuth_morris_pratt/*.py lcs/*.py
	ruff check rabin_karp/*.py knuth_morris_pratt/*.py lcs/*.py

.PHONY: format
format:
	ruff format rabin_karp/*.py knuth_morris_pratt/*.py lcs/*.py