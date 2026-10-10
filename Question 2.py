total_students = 0
total_marks = 0
passing_students = 0
failing_students = 0
highest_average = 0
lowest_average = 100
student_averages = []

print("Student Performance Analyzer")

while True:
    name = input("\nEnter student name (-1 to stop): ")

    if name == "-1":
        break

    total = 0

    # Enter marks of three subjects
    for i in range(3):
        if i == 0:
            marks = float(input("Enter Programming marks: "))
        elif i == 1:
            marks = float(input("Enter Mathematics marks: "))
        else:
            marks = float(input("Enter AI marks: "))

        total += marks

    average = total / 3
    student_averages.append(average)

    # Check pass or fail
    if average >= 50:
        print("Result: Pass")
        passing_students += 1
    else:
        print("Result: Fail")
        failing_students += 1

    print("Student Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", average)

    # Update class information
    total_students += 1
    total_marks += total

    if average > highest_average:
        highest_average = average

    if average < lowest_average:
        lowest_average = average

# Calculate class average
if total_students > 0:
    class_average = total_marks / (total_students * 3)

    # Count students above class average
    above_average = 0

    for average in student_averages:
        if average > class_average:
            above_average += 1

    print("\n----- Class Summary -----")
    print("Total Students:", total_students)
    print("Class Average:", class_average)
    print("Highest Average:", highest_average)
    print("Lowest Average:", lowest_average)
    print("Passing Students:", passing_students)
    print("Failing Students:", failing_students)
    print("Above Class Average:", above_average)
else:
    print("No student records entered.")
