# Joshua Perocho - Planit Technical Assessment — UI Automation

Python browser automation for the [Jupiter Toys](http://jupiter.cloud.planittesting.com) website. The suite uses pytest, pytest-bdd, and Playwright to check four customer journeys:

## Coverage

- **Homepage:** Verifies access to the home page.
- **Contact:** Checks the displayed error messages when an empty or incomplete feedback form is submitted. Submits a feedback form that contains the mandatory fields and repeats the test 5 times to ensure 100% pass rate. 
- **Shopping cart:** Adds products to the cart. Verifies prices, subtotals, and the total.

## Project layout

```text
.
├── conftest.py                     # Shared pytest fixtures and BDD tag handling
├── pytest.ini                      # Test configuration and base URL
├── requirements.txt                # Pinned Python dependencies
└── src/    
    ├── pages/                      # Page objects
    ├── services/                   # Page actions and assertions
    ├── tests/  
    │   ├── features/               # Gherkin scenarios
    │   └── steps/                  # pytest-bdd step definitions
    │       └── common_steps.py/    # Steps shared between tests
    └── util/                       # Test data, models, and shared helpers
```


`src/tests/features/` - Contains the BDD scenarios 

`src/tests/steps/`    - Contains the Step Definitions

`src/services/`       - Contains the workflow functions

`src/pages/`          - Contains the page interactions


## Requirements

- Python 3.10 or newer
- pip
- A Playwright-supported browser (Chromium is used by default)
- GNU Make and the Allure command-line tool are needed only for the Make targets and Allure reports

## Setup on macOS

Open Terminal in the project root and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Setup on Windows

Open PowerShell in the project root and run:

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

If PowerShell blocks virtual environment activation, use Command Prompt instead:

```bat
py -3 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Run the tests

After activating the virtual environment, these commands work on macOS Terminal, Windows PowerShell, and Command Prompt:

```text
python -m pytest
```

Run a single feature's scenarios:

```text
python -m pytest src/tests/steps/test_homepage.py
python -m pytest src/tests/steps/test_contact_page.py
python -m pytest src/tests/steps/test_cart.py
```

The base URL is configured in `pytest.ini` as `http://jupiter.cloud.planittesting.com`. Playwright runs headless by default. To watch the browser:

```text
python -m pytest --headed
```

To use a different Playwright browser, for example Firefox:

```text
python -m pytest --browser firefox
```

## Allure reports and Make targets

The Makefile creates Allure results and serves an Allure report. GNU Make and the Allure command-line tool must be installed and available on `PATH`. On macOS, run these in Terminal. On Windows, run them in WSL or Git Bash with GNU Make and Allure installed there; the Makefile's shell commands are Unix-style and are not intended for plain PowerShell or Command Prompt.

```bash
make test                    # Run the full suite and serve its Allure report
make smoke                   # Run tests tagged smoke
make regression              # Run tests tagged regression
make validation              # Run tests tagged validation
make homepage                # Run tests tagged homepage
make run TAG=smoke           # Run any pytest marker by name
make report                  # Serve the existing allure-results
make clean                   # Remove allure-results and allure-report
```

The marker descriptions are registered in `pytest.ini`. `smoke`, `regression`, and `validation` tag contact-form scenarios; `homepage` tags the homepage scenario. Cart scenarios carry the `regression` marker.

For Linux only, if browser system libraries are missing, install them with:

```bash
python -m playwright install --with-deps chromium
```

## Notes

- The feedback form success scenario is repeated five times through the custom `@repeat_5` tag handler in `conftest.py`.
- Dependencies are pinned in `requirements.txt`; `pyproject.toml` contains Ruff and Pylint line-length settings.
