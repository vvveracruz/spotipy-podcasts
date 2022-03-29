init:
	poetry update
	poetry install --dev

clean: 
	poetry run black src/
	rm -rf src/__pycache__
