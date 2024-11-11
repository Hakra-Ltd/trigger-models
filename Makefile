VENV := poetry run

lint: mypy ruff black
lint-fix: ruff-fix black-fix

# Linters
black:
	$(VENV) black --check trigger_models

black-fix:
	$(VENV) black trigger_models

ruff:
	$(VENV) ruff check trigger_models

ruff-fix:
	$(VENV) ruff check --fix trigger_models

mypy:
	$(VENV) mypy trigger_models

test:
	$(VENV) pytest -vvv

test-failed:
	$(VENV) pytest --last-failed -vvv;

