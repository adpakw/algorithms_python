.PHONY: stack_vs_queue
stack_vs_queue:
	pytest stack_vs_queue/test_stack_vs_queue.py

.PHONY: validate
validate:
	pytest validate/test_validate.py

.PHONY: merge_lists
merge_lists:
	pytest merge_lists/test_merge_lists.py

.PHONY: lint
lint:
	mypy stack_vs_queue/*.py validate/*.py merge_lists/*.py
	ruff check stack_vs_queue/*.py validate/*.py merge_lists/*.py

.PHONY: format
format:
	ruff format stack_vs_queue/*.py validate/*.py merge_lists/*.py