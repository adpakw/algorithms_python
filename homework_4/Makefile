.PHONY: validate_bst
validate_bst:
	pytest validate_bst/test_validate_bst.py

.PHONY: traversal
traversal:
	pytest traversal/test_traversal.py

.PHONY: hash_table
hash_table:
	pytest -v hash_table/test_hash_table.py

.PHONY: lint
lint:
	mypy validate_bst/*.py traversal/*.py hash_table/*.py
	ruff check validate_bst/*.py traversal/*.py hash_table/*.py

.PHONY: format
format:
	ruff format validate_bst/*.py traversal/*.py hash_table/*.py