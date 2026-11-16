import pytest
from student_result import (
    calculate_total,
    calculate_average,
    calculate_grade,
    check_result,
    analyze_student
)


# Unit Tests

def test_calculate_total():
    assert calculate_total([80, 90, 70]) == 240


def test_calculate_average():
    assert calculate_average([80, 90, 70]) == 80


def test_average_with_empty_marks():
    with pytest.raises(ValueError):
        calculate_average([])


def test_grade_A():
    assert calculate_grade(95) == "A"


def test_grade_B():
    assert calculate_grade(85) == "B"


def test_grade_C():
    assert calculate_grade(75) == "C"


def test_grade_D():
    assert calculate_grade(65) == "D"


def test_grade_E():
    assert calculate_grade(45) == "E"


def test_grade_F():
    assert calculate_grade(30) == "F"


def test_check_result_pass():
    assert check_result([80, 90, 70]) == "Pass"


def test_check_result_fail():
    assert check_result([80, 30, 70]) == "Fail"


# Integration Tests

def test_analyze_student():
    result = analyze_student("Arun", [90, 80, 70])

    assert result["Name"] == "Arun"
    assert result["Total"] == 240
    assert result["Average"] == 80
    assert result["Grade"] == "B"
    assert result["Result"] == "Pass"


def test_analyze_student_fail():
    result = analyze_student("Kumar", [90, 30, 70])

    assert result["Result"] == "Fail"


def test_analyze_student_empty_marks():
    with pytest.raises(ValueError):
        analyze_student("Ravi", [])
