init:
	poetry update
	poetry install

clean: 
	poetry run black src/
	rm -rf src/__pycache__
