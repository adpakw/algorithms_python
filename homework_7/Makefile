.PHONY: makeheap
makeheap:
	pytest makeheap/test_makeheap.py


.PHONY: k_th_minheap
k_th_minheap:
	pytest k_th_minheap/test_k_th_minheap.py

.PHONY: lint
lint:
	mypy makeheap/*.py k_th_minheap/*.py
	ruff check makeheap/*.py k_th_minheap/*.py

.PHONY: format
format:
	ruff format makeheap/*.py k_th_minheap/*.py