.PHONY: makeheap
makeheap:
	pytest makeheap/test_makeheap.py

.PHONY: iterative
iterative:
	pytest iterative/test_iterative.py

.PHONY: k_th
k_th:
	pytest k_th/test_k_th.py

.PHONY: lint
lint:
	mypy makeheap/*.py iterative/*.py k_th/*.py
	ruff check makeheap/*.py iterative/*.py k_th/*.py

.PHONY: format
format:
	ruff format makeheap/*.py iterative/*.py k_th/*.py