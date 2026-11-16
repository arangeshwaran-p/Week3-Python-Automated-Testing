from docx import Document
from docx.shared import Pt

doc = Document()

doc.add_heading("WEEK 3 - PYTHON AUTOMATED TESTING", 0)

doc.add_heading("1. Project Title", level=1)
doc.add_paragraph("Student Result Analyzer using Python and Pytest")

doc.add_heading("2. Objective", level=1)
doc.add_paragraph(
    "The objective of this project is to develop a Python application "
    "and verify its functionality using automated unit and integration tests."
)

doc.add_heading("3. Project Description", level=1)
doc.add_paragraph(
    "The Student Result Analyzer is a Python-based application developed "
    "to simplify the process of calculating and analyzing student academic "
    "results. The application accepts a student's name and subject marks "
    "and calculates the total marks, average, grade, and pass or fail status. "
    "It contains separate functions for each operation, making the program "
    "easy to understand, maintain, and test.\n\n"
    "The project uses Python for application development and Pytest as the "
    "automated testing framework. Automated testing helps verify that each "
    "function produces the expected output. Unit tests are written to check "
    "individual functions such as total calculation, average calculation, "
    "grade assignment, and pass or fail checking. Integration tests verify "
    "that these functions work correctly together through the complete "
    "student analysis process.\n\n"
    "The project also includes edge and error testing. For example, the "
    "application checks how the average calculation behaves when an empty "
    "marks list is provided. It raises a ValueError instead of producing an "
    "incorrect result. Different marks are also tested to verify all grade "
    "categories and both pass and fail conditions.\n\n"
    "The testing process follows the principles of Test-Driven Development "
    "(TDD), where test cases guide implementation and help identify errors "
    "early. The code and test cases are maintained in separate Python files. "
    "A README file explains the project, installation, and execution steps, "
    "while a separate testing document describes the test cases and results. "
    "This project demonstrates modular programming, automated testing, "
    "error handling, and software quality assurance."
)

doc.add_heading("4. Technologies Used", level=1)
doc.add_paragraph("Python 3.14\nPytest 9.2.0\nVisual Studio Code\nPowerShell")

doc.add_heading("5. Testing Methodology", level=1)
doc.add_paragraph(
    "Unit Testing: Tests individual functions independently.\n"
    "Integration Testing: Tests the complete student analysis process.\n"
    "Error Testing: Checks empty marks and expected exceptions.\n"
    "TDD: Uses test cases to guide implementation and verification."
)

doc.add_heading("6. Test Results", level=1)
doc.add_paragraph(
    "Total test cases: 14\n"
    "Passed: 14\n"
    "Failed: 0\n"
    "Testing command: py -m pytest -v"
)

doc.add_heading("7. Conclusion", level=1)
doc.add_paragraph(
    "The Student Result Analyzer was successfully developed and tested. "
    "All 14 automated test cases passed. This project provided practical "
    "experience in Python programming, Pytest, unit testing, integration "
    "testing, error handling, and software documentation."
)

doc.add_heading("8. Project Files", level=1)
doc.add_paragraph(
    "student_result.py\n"
    "test_student_result.py\n"
    "requirements.txt\n"
    "README.md\n"
    "TEST_DOCUMENTATION.md"
)

doc.save("Week3_Report.docx")
print("Word report created successfully!")
