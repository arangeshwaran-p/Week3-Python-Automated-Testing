

\# Continuous Integration Documentation



\## 1. Introduction

This project integrates Continuous Integration using

GitHub Actions to automate testing and code quality checks.



\## 2. CI Tool

GitHub Actions is used to execute the workflow automatically

when code is pushed to the main branch or a pull request

is created.



\## 3. Pipeline Stages

\- Checkout source code

\- Set up Python environment

\- Install dependencies

\- Run Flake8

\- Execute Pytest

\- Generate HTML test report

\- Upload test report as an artifact



\## 4. Testing Tools

Pytest is used for automated testing.

Flake8 checks Python code quality.

Pytest HTML generates an HTML testing report.



\## 5. Run Locally



Install dependencies:

pip install -r requirements.txt



Run tests:

python -m pytest -v



Run linting:

python -m flake8 student\_result.py test\_student\_result.py



Generate report:

python -m pytest -v --html=report.html --self-contained-html



\## 6. Test Results

Local verification:

14 tests passed.

0 tests failed.



\## 7. GitHub Actions Verification

Push changes to the main branch.

Open the GitHub repository.

Select Actions.

Open the Python CI Pipeline workflow.

Check the build logs and test report artifact.



\## 8. Failure Handling

The workflow stops and reports failure if

Flake8 or Pytest returns an error.



\## 9. Conclusion

The CI pipeline improves software quality by automating

code checking, testing, and report generation.





