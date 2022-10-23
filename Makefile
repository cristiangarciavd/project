DEATULT_TAGS=api
TAGS="$(DEATULT_TAGS)"
REPORT_FILE=./reports/cucumber_report.json
ENV="test"
BROWSER="CHROME"
REMOTE_BROWSER="CHROME"

DEFAULT_CONFIG_JSON=.configuration.json
CONFIG_JSON="${DEFAULT_CONFIG_JSON}"
DEFAULT_ENVIRONMENT_JSON=.environment.json
ENVIRONMENT_JSON="${DEFAULT_ENVIRONMENT_JSON}"

setup:
	@echo "Installing dependencies..."
	python -m pipenv install -d
	@echo "Setup cucumber-html-reporter"
	python -m pipenv run npm install cucumber-html-reporter --save-dev 
	@echo "Setup Done!"

static_code_analysis:
	@echo "Static Code analysis"
	python -m pipenv run pylint main/
	python -m pipenv run pylint tests/
	python -m pipenv run flake8 main/ --benchmark
	python -m pipenv run flake8 tests/ --benchmark
	python -m pipenv run pycodestyle main/ --benchmark
	python -m pipenv run pycodestyle tests/ --benchmark

all_test:
	@echo "Executing all testing scenarios"
	python -m pipenv run pytest --cache-clear

test:
	@echo "Executing testing scenarios with TAGS: $(TAGS)"
	@echo "Report file: $(REPORT_FILE)"
	python -m pipenv run pytest --cache-clear --cucumber-json="$(REPORT_FILE)" -vsm "$(TAGS)"
	@echo "Finished testing."

report:
	@echo "Generating html report"
	python -m pipenv run node cucumberReportGenerator.js