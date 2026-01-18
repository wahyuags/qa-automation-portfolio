# QA Automation Portfolio – Login Test Suite

**Wahyu Agustiar**
QA Automation Engineer (Remote)

---

## Overview

This repository demonstrates a production‑ready UI automation framework built with Selenium WebDriver and Pytest.

The project reflects how automated UI tests are structured and maintained in real‑world QA teams, with a focus on long‑term stability, maintainability, and clear test evidence.

The framework targets a realistic authentication flow to showcase core QA automation skills that scale to larger systems.



## Application Under Test

* URL: [https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)
* Feature: Login authentication
* Test type: Functional UI automation



## Key Capabilities

* Page Object Model (POM) for clean separation of concerns
* Explicit waits to reduce flaky test behavior
* Centralized WebDriver lifecycle via Pytest fixtures
* Automatic screenshot capture on unexpected failures
* Self‑contained HTML reports with embedded screenshots
* Clear distinction between expected failures and real defects



## Technology Stack

* Python 3
* Selenium WebDriver
* Pytest
* pytest‑html
* webdriver‑manager



## Project Structure

```
project-root/
├── core/                # Base driver and base page logic
├── pages/               # Page Object classes
├── tests/               # Test scenarios
├── utils/               # Helpers (screenshots, utilities)
├── config/              # Configuration and constants
├── reports/             # Generated HTML reports
├── screenshots/         # Failure screenshots
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```



## Installation

### Prerequisites

* Python 3.8 or higher (recommended: 3.12)
* Google Chrome installed
* Internet connection for WebDriver download

### Setup

```bash
git clone https://github.com/wahyuags/qa-automation-portfolio.git
cd qa-automation-portfolio

python -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\\Scripts\\activate     # Windows

pip install -r requirements.txt
```


## Running Tests

Run the full test suite:

```bash
pytest -v
```

Generate an HTML report with embedded screenshots:

```bash
pytest --html=reports/report.html --self-contained-html
```

Generated artifacts:

* reports/report.html
* screenshots/*.png (for unexpected failures)



## Expected Failures vs Defects

Negative scenarios such as invalid login credentials are treated as expected outcomes and are considered successful test executions.

The following are treated as defects:

* Unexpected timeouts
* Missing or changed UI elements
* Application crashes or navigation failures
* Inconsistent or non‑deterministic behavior

Screenshots and reports are generated to support investigation and root‑cause analysis.



## Bug Reporting Guidelines

When reporting an issue, include:

1. Clear issue title
2. Steps to reproduce
3. Expected and actual behavior
4. Environment details (OS, browser, Python version)
5. HTML report and/or screenshot
6. Relevant stacktrace

This mirrors professional QA defect‑reporting standards.


## QA Principles Demonstrated

* Stability over test quantity
* Deterministic test execution
* Explicit waits over static sleeps
* Readable assertions
* Evidence‑based reporting



## Intended Use

* QA automation portfolio for remote roles
* Reference framework for UI automation projects
* Demonstration of professional QA practices


## Notes

This project is intentionally minimal and focused. Optional future enhancements include:

* CI integration (GitHub Actions)
* Test tagging (smoke / regression)
* Advanced reporting (Allure)
* Retry strategies for unstable environments
