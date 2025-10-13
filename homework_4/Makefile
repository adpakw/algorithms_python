.PHONY: validate_bst
validate_bst:
	pytest validate_bst/test_validate_bst.py

.PHONY: traversal
traversal:
	pytest traversal/test_traversal.py

.PHONY: balanced_binary_tree
balanced_binary_tree:
	pytest balanced_binary_tree/test_balanced_binary_tree.py

.PHONY: lint
lint:
	mypy validate_bst/*.py traversal/*.py balanced_binary_tree/*.py
	ruff check validate_bst/*.py traversal/*.py balanced_binary_tree/*.py

.PHONY: format
format:
	ruff format validate_bst/*.py traversal/*.py balanced_binary_tree/*.py