.PHONY: runserver coverage

runserver:
	# docker compose up database -d # Caso seja necessario subir o banco
	uvicorn app.main:app --reload --host=localhost --port=8080

coverage:
	coverage run -m unittest
	coverage report --fail-under 95
	coverage html
