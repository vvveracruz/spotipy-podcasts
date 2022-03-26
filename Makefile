default:
	poetry run black --quiet src/
	poetry run python src/main.py

init:
	poetry update
	poetry install