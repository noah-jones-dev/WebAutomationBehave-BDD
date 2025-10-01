
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

VIDEOS HERE

## Project Structure

- [app](./app/) – Contains the main application code or scripts used for testing setup.  
- [features](./features/) – Holds all Behave feature files and related test logic.  
    - [steps](./features/steps/) – Step definitions for Behave scenarios.  
        - [common_steps](./features/steps/common_steps/) – Generic steps used across multiple tests.  
        - [product_availability_steps](./features/steps/product_availability_steps/) – Steps related to checking product availability.  
        - [search_product_steps](./features/steps/search_product_steps/) – Steps for searching and selecting products.  
        - [translation_steps](./features/steps/translation_steps/) – Steps for verifying translations or localized content.  
    - [tests](./features/tests/) – Organized feature test files.  
        - [product_availability_tests](./features/tests/product_availability_tests/) – Feature files for product availability scenarios.  
        - [search_product_tests](./features/tests/search_product_tests/) – Feature files for product search scenarios.  
        - [translation_tests](./features/tests/translation_tests/) – Feature files for translation scenarios.  
    - [environment](./features/environment/) – Setup and teardown hooks for Behave tests (before/after scenario or feature).  
- [framework](./framework/) – Core framework utilities, reusable components, and helpers.  
    - [fields](./framework/fields/) – Page element abstractions following the Page Object Model.  
        - [button_field](./framework/fields/button_field/) – Button element interactions.  
        - [checkbox_field](./framework/fields/checkbox_field/) – Checkbox element interactions.  
        - [element_base](./framework/fields/element_base/) – Base class for all page elements.  
        - [link_field](./framework/fields/link_field/) – Link element interactions.  
        - [list_field](./framework/fields/list_field/) – List element interactions.  
        - [nav_field](./framework/fields/nav_field/) – Navigation element interactions.  
        - [select_field](./framework/fields/select_field/) – Dropdown/select element interactions.  
        - [static_field](./framework/fields/static_field/) – Static text elements.  
        - [text_field](./framework/fields/text_field/) – Input or text box elements.  
    - [helpers](./framework/helpers/) – Utility modules to assist tests.  
        - [verifications](./framework/helpers/verifications/) – Verification/assertion helpers for UI elements.  
            - [verify_base](./framework/helpers/verifications/verify_base/) – Base verification logic.  
            - [verify_button](./framework/helpers/verifications/verify_button/) – Button verification helpers.  
            - [verify_checkbox](./framework/helpers/verifications/verify_checkbox/) – Checkbox verification helpers.  
            - [verify_link](./framework/helpers/verifications/verify_link/) – Link verification helpers.  
            - [verify_list](./framework/helpers/verifications/verify_list/) – List verification helpers.  
            - [verify_select](./framework/helpers/verifications/verify_select/) – Dropdown verification helpers.  
            - [verify_static](./framework/helpers/verifications/verify_static/) – Static element verification.  
            - [verify_text](./framework/helpers/verifications/verify_text/) – Text element verification.  
        - [scroll_directions](./framework/helpers/scroll_directions/) – Helpers for scrolling in different directions.  
        - [waits](./framework/helpers/waits/) – Custom wait conditions for elements.  
        - [window_utilities](./framework/helpers/window_utilities/) – Browser window/tab utilities.  
- [pages](./pages/) – Page Object Model (POM) classes representing web pages.  
    - [base_page](./pages/base_page/) – Base class for all page objects.  
    - [crayons_page](./pages/crayons_page/) – Page object for the Crayons page.  
    - [home_page](./pages/home_page/) – Page object for the Home page.  
    - [product_detail_page](./pages/product_detail_page/) – Page object for Product Detail page.  
    - [product_listing_page](./pages/product_listing_page/) – Page object for Product Listing page.  
- [report/results](./report/results/) – Folder where test execution reports or logs are saved.  
- [tips](./tips/) – Additional documentation, guides, or troubleshooting tips.  
    - [running_reports.txt](./tips/running_reports.txt) – Notes on running and interpreting test reports.  
