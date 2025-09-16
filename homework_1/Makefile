.PHONY: palindrome
palindrome:
	pytest palindrome/test_palindrome.py

.PHONY: lint
lint:
	mypy palindrome/*.py
	ruff check palindrome/*.py

.PHONY: format
format:
	ruff format palindrome/*.py