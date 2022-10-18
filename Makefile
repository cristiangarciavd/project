DEFAULT_TAGS=api
TAGS="$(DEFAULT_TAGS)"

ENV="test"
BROWSER="CHROME"
REMOTE_BROWSER="CHROME"

DEFAULT_CONFIG_JSON=.configuration.json
CONFIG_JSON="$(DEFAULT_CONFIG_JSON)"
DEFAULT_ENVIRONMENT_JSON=.environment.json
ENVIRONMENT_JSON="$(DEFAULT_ENVIRONMENT_JSON)"

setup:
	python -m pipenv install

static_code_analysis:
	@echo "Static Code Analysis"
	python -m pipenv run pylint main/
	python -m pipenv run flake8 main/ --benchmark
	python -m pipenv run pycodestyle main/ --benchmark