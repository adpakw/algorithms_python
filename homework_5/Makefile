.PHONY: traversal
traversal:
	pytest traversal/test_traversal.py

.PHONY: balanced_binary_tree
balanced_binary_tree:
	pytest balanced_binary_tree/test_balanced_binary_tree.py

.PHONY: lint
lint:
	mypy tracer/*.py traversal/*.py balanced_binary_tree/*.py
	ruff check tracer/*.py traversal/*.py balanced_binary_tree/*.py

.PHONY: format
format:
	ruff format tracer/*.py traversal/*.py balanced_binary_tree/*.py