.PHONY: two_sum
two_sum:
	pytest two_sum/test_two_sum.py

.PHONY: traversal
traversal:
	pytest traversal/test_traversal.py

.PHONY: hash_table
hash_table:
	pytest hash_table/test_hash_table.py

.PHONY: lint
lint:
	mypy two_sum/*.py traversal/*.py hash_table/*.py
	ruff check two_sum/*.py traversal/*.py hash_table/*.py

.PHONY: format
format:
	ruff format two_sum/*.py traversal/*.py hash_table/*.py