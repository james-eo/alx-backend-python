# 0x03. Unittests and Integration Tests

## Description

This project focuses on creating and executing unit and integration tests in Python. Unit tests ensure individual functions return expected results for different sets of inputs, while integration tests check interactions between various parts of the code. The project aims to provide practical experience with testing patterns such as mocking, parameterization, and fixtures.

## Learning Objectives

By the end of this project, you should be able to:
- Understand the difference between unit and integration tests.
- Apply common testing patterns like mocking, parameterization, and using fixtures.
- Create tests using the `unittest` framework and other tools like `parameterized`.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7).
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should adhere to the `pycodestyle` style (version 2.5).
- All files must be executable.
- All modules should have documentation.
- All classes should have documentation.
- All functions should have documentation.
- Documentation should be detailed and explanatory.
- All functions and coroutines must be type-annotated.

## File Structure

- `utils.py`: Contains utility functions.
- `client.py`: Contains the `GithubOrgClient` class for interacting with the GitHub API.
- `fixtures.py`: Provides fixture data for testing.
- `test_utils.py`: Contains unit tests for `utils.py`.
- `test_client.py`: Contains unit and integration tests for `client.py`.

## Installation

Ensure you have Python 3.7 installed. Clone the repository and make the files executable:

```bash
chmod +x utils.py client.py fixtures.py test_utils.py test_client.py
