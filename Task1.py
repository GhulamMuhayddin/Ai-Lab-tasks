marks = float(input("Enter marks: "))

if 90 <= marks <= 100:
    grade = "A"
elif 80 <= marks < 90:
    grade = "B"
elif 70 <= marks < 80:
    grade = "C"
elif 60 <= marks < 70:
    grade = "D"
elif 50 <= marks < 60:
    grade = "E"
elif 0 <= marks < 50:
    grade = "F"
else:
    grade = "Invalid Marks"

print("Grade:", grade)
