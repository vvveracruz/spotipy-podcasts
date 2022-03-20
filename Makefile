default:
	poetry run black --quiet src/
	poetry run python src/spotipy-ctrl.py