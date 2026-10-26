.PHONY: smoke regression validation homepage test report clean

ALLURE_RESULTS = allure-results

all: 
	@pytest -v --alluredir=$(ALLURE_RESULTS) --clean-alluredir; status=$$?; allure serve $(ALLURE_RESULTS); exit $$status

smoke:
	@pytest -m smoke -v --alluredir=$(ALLURE_RESULTS) --clean-alluredir; status=$$?; allure serve $(ALLURE_RESULTS); exit $$status

regression:
	@pytest -m regression -v --alluredir=$(ALLURE_RESULTS) --clean-alluredir; status=$$?; allure serve $(ALLURE_RESULTS); exit $$status

validation:
	@pytest -m validation -v --alluredir=$(ALLURE_RESULTS) --clean-alluredir; status=$$?; allure serve $(ALLURE_RESULTS); exit $$status

homepage:
	@pytest -m homepage -v --alluredir=$(ALLURE_RESULTS) --clean-alluredir; status=$$?; allure serve $(ALLURE_RESULTS); exit $$status

test:
	@pytest -v --alluredir=$(ALLURE_RESULTS) --clean-alluredir; status=$$?; allure serve $(ALLURE_RESULTS); exit $$status

run:
	@pytest -m "$(TAG)" -v --alluredir=$(ALLURE_RESULTS) --clean-alluredir; \
	status=$$?; \
	allure serve $(ALLURE_RESULTS); \
	exit $$status

report:
	allure serve $(ALLURE_RESULTS)

clean:
	rm -rf $(ALLURE_RESULTS) allure-report
