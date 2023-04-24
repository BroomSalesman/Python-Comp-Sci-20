"""def letter_grade(exam_grade):
    if exam_grade >= 90:
        grade = "A"
    elif 80 <= exam_grade < 90:
        grade = "B"
    elif 70 <= exam_grade < 80:
        grade = "C"
    elif 60 <= exam_grade < 70:
        grade = "D"    
    else:
        grade = "F"
    
    return grade"""

def letter_grade(exam_grade):
    if exam_grade >= 90:
        return "A"
    elif exam_grade >= 80:
        return "B"
    elif exam_grade >= 70:
        return "C"
    elif exam_grade >= 60:
        return "D"
    else:
        return "F"


assert letter_grade(83) == "B"
assert letter_grade(75) == "C"
assert letter_grade(80) == "B"
assert letter_grade(90) == "A"
assert letter_grade(89.9) == "B"
assert letter_grade(55) == "F"
assert letter_grade(45) == "F"
assert letter_grade(69.7) == "D"

print("All assertions passed. Function works as expc")
