# Translation API Automated Test Framework

## Overview

This project is a Python-based automated test framework designed to validate a simple translation API. It uses a fully in-memory mock of the API, allowing for rapid, isolated, and repeatable tests without any external dependencies or network calls.

---

## Project Structure
````
project_root/
│
├── core/
│ ├── init.py
│ └── api_client.py  # Mock API logic
│
├── tests/
│ ├── init.py
│ └── test_translator_api.py  # Test cases
│
├── config.ini  # API endpoint configuration
├── pytest.ini  # Pytest configuration
├── requirements.txt  # Python dependencies
├── conftest.py  # Global fixtures and setup
└── README.md  # Project documentation
````
---

## Setup Instructions

1. **Clone the repository** 
```
git clone <your-repo-url>  
cd <your-repo-folder>
```

2. **Setup project environment** 

2.1. **Create and activate a virtual environment (optional but recommended)**  
```
python -m venv venv  
source venv/bin/activate # On Windows: venv\Scripts\activate
```
2.2. **Running the Framework in Docker (optional)**

You can run this test framework in Docker for full environment isolation and portability.  
Below are instructions for running with and without test report generation.

#### 2.2.1. Build the Docker Image

From your project root, run:
```
docker build -t translation-api-test-framework .
```

#### 2.2.2. Run Tests in Docker

  ```
  docker run --rm translation-api-test-framework
  ```

3. **Install dependencies**
```
pip install -r requirements.txt
```
4. **Run the tests**

Simply run:  
```
pytest
```

or, for more verbose output:
```
pytest -v
```
## Assumptions & Decisions

- No real network calls: All API requests are intercepted and handled by a Python class mock (TranslationAPIMock), so no internet access or live API endpoint is needed
- Pythonic & maintainable: The mock logic is encapsulated in a class for extensibility and clarity
- Global patching: The framework uses a global pytest fixture (conftest.py) to patch requests.get for all tests, keeping test code clean
- Extensibility: The framework is ready for more endpoints, HTTP methods, or payload-based requests if required
- No external services required: This framework is fully self-contained for unit/integration level testing of Python HTTP client code

## Test Reports
### Pytest HTML Report
To generate a simple HTML test report:

1. **Install the plugin:**
    ```
    pip install pytest-html
    ```

2. **Run tests with HTML output:**
    ```
    pytest --html=reports/pytest/report.html --self-contained-html
    ```

3. **View the report:**
   Open `report.html` in your web browser.

---
### Allure Report

For advanced, interactive test reports:

1. **Install the plugin:**
    ```
    pip install allure-pytest
    ```

2. **Run tests and collect Allure results:**
    ```
    pytest --alluredir=reports/allure-results
    ```

3. **Install Allure commandline:**

    - **Mac:**  
      ```
      brew install allure
      ```
    - **Linux (Debian/Ubuntu):**  
      ```
      sudo apt install allure
      ```
    - **Windows:**  
      - Download the latest [Allure commandline zip](https://github.com/allure-framework/allure2/releases)  
      - Extract it and add the `bin` folder to your system `PATH`.

    - **Alternative for all OS:**  
      - Download from [Allure Releases](https://github.com/allure-framework/allure2/releases)  
      - Or use Docker:
        ```
        docker run -p 5050:5050 -v $(pwd)/allure-results:/app/allure-results -v $(pwd)/allure-report:/app/allure-report frankescobar/allure-docker-service
        ```

4. **Generate and open the report:**
    ```
    allure generate reports/allure-results -o reports/allure-report --clean
    allure open allure-report
    ```

5. **View the interactive Allure dashboard** in your browser.

---

## Notes

- Dependencies: Uses pytest for testing and requests for simulating HTTP calls
- Python version: Compatible with Python 3.7+
- Adding more tests: Simply add more functions in tests/test_translator_api.py or new files under tests/
- Mock customization: To support more endpoints or logic, extend core/api_client.py