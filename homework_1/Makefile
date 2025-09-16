.PHONY: palindrome
palindrome:
	pytest palindrome/test_palindrome.py

.PHONY: sum
sum:
	pytest sum/test_sum.py

.PHONY: lint
lint:
	mypy palindrome/*.py sum/*.py
	ruff check palindrome/*.py sum/*.py

.PHONY: format
format:
	ruff format palindrome/*.py sum/*.py