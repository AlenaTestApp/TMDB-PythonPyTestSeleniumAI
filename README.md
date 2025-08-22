# TMDB Automation Project

## Overview

Project Automates Test scenarios for TMDB using Python and PyTest. The Framework uses POM structure.
The project is designed to be extended with advanced scenarios,
including **AI-powered visual comparison of images**

## Project Structure

TMDB_AUTOMATION/
│
├── configs/ # Configuration files: test data, URLs, env settings
│ ├── __init__.py
│ ├── credentials.py
│ ├── endpoints.py
│ └── env_settings.py
│
├── pages/ # POM classes
│ ├── __init__.py
│ ├── locators.py
│ └── login_page.py
│
├── tests/ # Test cases
│ ├── __init__.py
│ └── test_login.py
│
├── utils/ # TBU
│ └── __init__.py
│
├── conftest.py # Pytest fixtures and setup
├── README.md # Project documentation
└── .gitignore # Git ignore rules



## How to run tests

To run all tests:

```bash
pytest -s tests/
```

To run only login tests:

```bash
pytest -s tests/test_login.py
```
