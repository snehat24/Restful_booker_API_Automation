# Playwright API Testing Framework

API automation framework built using Python, Pytest, and Playwright.

## Features
## Features

* CRUD API Testing (GET, POST, PUT, PATCH, DELETE)
* Authentication Token Handling
* API Chaining
* Dynamic Booking ID Handling
* Pytest Fixtures
* Dynamic Test Data
* Payload Separation
* Reusable Headers Utility
* Base URL Configuration
* JSON Response Validation
* Response Header Validation
* Logging
* HTML Reports
* Negative Test Scenarios
* Modular Framework Structure


## Tech Stack

* Python
* Pytest
* Playwright API Testing
* pytest-html

## Project Structure

```text
logs/
tests/
payloads/
utils/
reports/
conftest.py
config.py
pytest.ini
requirements.txt
```

## How to Run Tests

Run all tests:

```bash
pytest
```

Run single test:

```bash
pytest tests/test_get_booking.py
```

## Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

## Author

Sneha
