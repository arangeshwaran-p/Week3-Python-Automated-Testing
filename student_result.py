# Student Result Analyzer

def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    if len(marks) == 0:
        raise ValueError("Marks cannot be empty")
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


def check_result(marks):
    for mark in marks:
        if mark < 40:
            return "Fail"
    return "Pass"


def analyze_student(name, marks):
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    result = check_result(marks)

    return {
        "Name": name,
        "Total": total,
        "Average": average,
        "Grade": grade,
        "Result": result
    }
