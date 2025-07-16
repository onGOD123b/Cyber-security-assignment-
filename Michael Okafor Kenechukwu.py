
#Michael Okafor Kenechukwu
score = float(input("Enter STUDENT'S score: "))


if (score >= 70) :
    grade= "A"
if (score < 70) and (score >= 60):
    grade= "B"
if (score < 60) and (score >=50):
    grade="C"
if (score <50) and (score>= 45):
    grade="D"
if (score <45) and (score>=40):
    grade="E"
if (score <40):
    grade="F"

print("your grade is:", grade)

