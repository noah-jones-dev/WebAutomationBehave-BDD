
# Web Automation Behave Project

## Description

Fully functional web automation framework written in Python using the Behave(BDD) testing framework automating Crayola's storefront website!

## Overview

**WebAutomationPython** is a web automation testing framework built with [Behave](https://behave.readthedocs.io/en/stable/) (a Python BDD framework) and [Selenium](https://www.selenium.dev/).  
It follows the **Page Object Model (POM)** design pattern to keep test cases clean, reusable, and easy to maintain.  

The framework is designed to:  
- Automate end-to-end web UI tests using BDD-style scenarios.  
- Provide readable test results in console or JUnit XML format (CI/CD friendly).  
- Support scalability for adding new test cases, features, and page components.  
- Run locally or be integrated into CI/CD pipelines (e.g., GitHub Actions, Jenkins).  

This project is ideal for:  
- Demonstrating automation skills in a Python-based portfolio project.  
- QA engineers learning BDD automation with Behave + Selenium.  
- Teams needing a structured, maintainable Selenium + Behave setup. ## Tech Stack

**Language & Frameworks:**  
- Language: Python 3.12+  
- BDD Framework: Behave  
- Web Driver: Selenium  
- Test Reporting: Allure

**Tools & Utilities:**  
- Browser Driver: ChromeDriver (managed with [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager))  
- Version Control: Git/GitHub  
- Text Editor: VS Code (with extensions)
## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Live Tests](#live-tests)
- [Project Structure](#project-structure)
## Prerequisites

Before installing, make sure you have the following:
- [Python 3.12+](https://www.python.org/downloads/) installed  
- Google Chrome (latest version)  
- An IDE or code editor of your choice:
  - VS Code (with Python + Behave extensions recommended)
  - PyCharm (with professional version or the Gherkin plugin on community version)
  - Any editor that supports Python

To verify installation:
```bash
python --version
pip --version
```
> [!NOTE]
> Make sure the Python installation path is added to your system PATH.

## Installation

Clone the repository:
```bash
git clone https://github.com/NoahsJones/WebAutomationBehave.git
cd WebAutomationBehave
```
### Dependencies

This project uses the following Python packages:
- behave – BDD test framework
- selenium – Browser automation
- webdriver-manager – Automatically manages browser drivers

To install dependencies, run:
```bash
pip install behave selenium webdriver-manager
```
If you need to add a new dependency manually:
```bash
pip install <package-name>
```
Add the recommended extensions from VS Code:
- Behave VSC
- Cucumber (Gherkin) Full support
- Pylance
- Python
- Python Debugger
- Python Environments 
- Python Type Hint
- Test Explorer UI
## Running Tests

### Run all tests
```bash
behave
```
Run a specific feature file:
```bash
behave features/example.feature
```
Run tests with a specific tag:
```bash
behave --tags=@smoke
```
Run tests and show detailed logging:
```bash
behave -v
```
> [!TIP]
> Test results will be shown directly in the terminal by default.
> For advanced reporting, you can integrate with Allure Behave:
```bash
pip install allure-behave
behave -f allure_behave.formatter:AllureFormatter -o Reports/Results
allure serve Reports/Results
```
## Live Tests

![FindAProduct](https://github.com/user-attachments/assets/abb69c90-276a-42be-b32a-afab4f4fbd61)

![VerifyTranslation](https://github.com/user-attachments/assets/3be2a3c7-ca7f-44f4-85e0-c7aaf4da5904)

## Project Structure

- [app](app/) – Contains the main application code or scripts used for testing setup.  
- [features](features/) – Holds all Behave feature files and related test logic.  
    - [steps](features/steps/) – Step definitions for Behave scenarios.  
        - [common_steps.py](features/steps/common_steps.py) – Generic steps used across multiple tests.  
        - [product_availability_steps.py](features/steps/product_availability_steps.py) – Steps related to checking product availability.  
        - [search_product_steps.py](features/steps/search_product_steps.py) – Steps for searching and selecting products.  
        - [translation_steps.py](features/steps/translation_steps.py) – Steps for verifying translations or localized content.  
    - [tests](features/tests/) – Organized feature test files.  
        - [product_availability_tests.py](features/tests/product_availability_tests.py) – Feature files for product availability scenarios.  
        - [search_product_tests.py](features/tests/search_product_tests.py) – Feature files for product search scenarios.  
        - [translation_tests.py](features/tests/translation_tests.py) – Feature files for translation scenarios.  
    - [environment](features/environment/) – Setup and teardown hooks for Behave tests (before/after scenario or feature).  
- [framework](framework/) – Core framework utilities, reusable components, and helpers.  
    - [fields](framework/fields/) – Page element abstractions following the Page Object Model.  
        - [button_field.py](framework/fields/button_field.py) – Button element interactions.  
        - [checkbox_field.py](framework/fields/checkbox_field.py) – Checkbox element interactions.  
        - [element_base.py](framework/fields/element_base.py) – Base class for all page elements.  
        - [link_field.py](framework/fields/link_field.py) – Link element interactions.  
        - [list_field.py](framework/fields/list_field.py) – List element interactions.  
        - [nav_field.py](framework/fields/nav_field.py) – Navigation element interactions.  
        - [select_field.py](framework/fields/select_field.py) – Dropdown/select element interactions.  
        - [static_field.py](framework/fields/static_field.py) – Static text elements.  
        - [text_field.py](framework/fields/text_field.py) – Input or text box elements.  
    - [helpers](framework/helpers/) – Utility modules to assist tests.  
        - [verifications](framework/helpers/verifications/) – Verification/assertion helpers for UI elements.  
            - [verify_base.py](framework/helpers/verifications/verify_base.py) – Base verification logic.  
            - [verify_button.py](framework/helpers/verifications/verify_button.py) – Button verification helpers.  
            - [verify_checkbox.py](framework/helpers/verifications/verify_checkbox.py) – Checkbox verification helpers.  
            - [verify_link.py](framework/helpers/verifications/verify_link.py) – Link verification helpers.  
            - [verify_list.py](framework/helpers/verifications/verify_list.py) – List verification helpers.  
            - [verify_select.py](framework/helpers/verifications/verify_select.py) – Dropdown verification helpers.  
            - [verify_static.py](framework/helpers/verifications/verify_static.py) – Static element verification.  
            - [verify_text.py](framework/helpers/verifications/verify_text.py) – Text element verification.  
        - [scroll_directions.py](framework/helpers/scroll_directions.py) – Helpers for scrolling in different directions.  
        - [waits.py](framework/helpers/waits.py) – Custom wait conditions for elements.  
        - [window_utilities.py](framework/helpers/window_utilities.py) – Browser window/tab utilities.  
- [pages](pages/) – Page Object Model (POM) classes representing web pages.  
    - [base_page.py](pages/base_page.py) – Base class for all page objects.  
    - [crayons_page.py](pages/crayons_page.py) – Page object for the Crayons page.  
    - [home_page.py](pages/home_page.py) – Page object for the Home page.  
    - [product_detail_page.py](pages/product_detail_page.py) – Page object for Product Detail page.  
    - [product_listing_page.py](pages/product_listing_page.py) – Page object for Product Listing page.  
- [report/results](report/results/) – Folder where test execution reports or logs are saved.  
- [tips](tips/) – Additional documentation, guides, or troubleshooting tips.  
    - [running_reports.txt](tips/running_reports.txt) – Notes on running and interpreting test reports.  
