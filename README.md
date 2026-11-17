

\# Python Student Result Analyzer - CI Project



\## Project Description

This project analyzes student marks and calculates total,

average, grade, and pass/fail results.



\## Technologies Used

\- Python 3.12+

\- Pytest

\- Flake8

\- Pytest HTML

\- GitHub Actions



\## Project Features

\- Calculate total marks

\- Calculate average marks

\- Assign grades

\- Check pass or fail status

\- Analyze student results



\## Automated Testing

Run tests:

python -m pytest -v



Generate HTML report:

python -m pytest -v --html=report.html --self-contained-html



\## Code Quality

Run Flake8:

python -m flake8 student\_result.py test\_student\_result.py



\## Install Dependencies

pip install -r requirements.txt



\## Continuous Integration

GitHub Actions automatically runs:

1\. Python environment setup

2\. Dependency installation

3\. Flake8 code checking

4\. Pytest automated testing

5\. HTML report generation

6\. Test report upload



\## CI Workflow

.github/workflows/python-ci.yml



\## Test Results

14 automated test cases passed successfully

during local verification.



