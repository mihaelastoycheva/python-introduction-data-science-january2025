def grade_in_words(grade: float) -> str:
    words = ""
    if 2.00 <= grade <= 2.99:
        words = "Fail"
    elif 3.00 <= grade <= 3.49:
        words = "Poor"
    elif 3.50 <= grade <= 4.49:
        words = "Good"
    elif 4.50 <= grade <= 5.49:
        words = "Very Good"
    elif 5.50 <= grade <= 6.00:
        words = "Excellent"
    return words


grade = float(input())

print(grade_in_words(grade))