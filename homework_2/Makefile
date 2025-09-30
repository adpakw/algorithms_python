.PHONY: stack_vs_queue
stack_vs_queue:
	pytest stack_vs_queue/test_stack_vs_queue.py

.PHONY: validate
validate:
	pytest validate/test_validate.py

.PHONY: prime
prime:
	pytest prime/test_prime.py

.PHONY: lint
lint:
	mypy stack_vs_queue/*.py validate/*.py prime/*.py
	ruff check stack_vs_queue/*.py validate/*.py prime/*.py

.PHONY: format
format:
	ruff format stack_vs_queue/*.py validate/*.py prime/*.py