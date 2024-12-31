def get_grade(score1, score2, score3):
    gpa = (score1 + score2 + score3) / 3
    if 90 <= gpa <= 100:
        return "A"
    elif 80 <= gpa < 90:
        return "B"
    elif 70 <= gpa < 80:
        return "C"
    elif 60 <= gpa < 70:
        return "D"
    else:
        return "F"

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True