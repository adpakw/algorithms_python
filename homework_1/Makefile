.PHONY: palindrome
palindrome:
	pytest palindrome/test_palindrome.py

.PHONY: sum
sum:
	pytest sum/test_sum.py

.PHONY: prime
prime:
	pytest prime/test_prime.py

.PHONY: lint
lint:
	mypy palindrome/*.py sum/*.py prime/*.py
	ruff check palindrome/*.py sum/*.py prime/*.py

.PHONY: format
format:
	ruff format palindrome/*.py sum/*.py prime/*.py