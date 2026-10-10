names = []
averages = []

total_students = 0
total_marks = 0
passing_students = 0
failing_students = 0

highest_average = 0
lowest_average = 100

# Enter student records
while True:
    name = input("\nEnter student name (-1 to stop): ")

    if name == "-1":
        break

    total = 0

    subjects = ["Programming", "Mathematics", "Artificial Intelligence"]

    # Enter marks using for loop
    for subject in subjects:
        marks = float(input("Enter " + subject + " marks: "))
        total += marks

    average = total / 3

    names.append(name)
    averages.append(average)

    print("Total Marks:", total)
    print("Average Marks:", average)

    # Check pass or fail
    if average >= 50:
        print("Result: Pass")
        passing_students += 1
    else:
        print("Result: Fail")
        failing_students += 1

    # Update class information
    total_students += 1
    total_marks += total

    if total_students == 1:
        highest_average = average
        lowest_average = average
    else:
        if average > highest_average:
            highest_average = average

        if average < lowest_average:
            lowest_average = average

# Calculate class average
if total_students > 0:
    class_average = total_marks / (total_students * 3)

    above_average = 0

    for average in averages:
        if average > class_average:
            above_average += 1

    # Compare students using nested loops
    print("\n===== Student Comparisons =====")

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if averages[i] > averages[j]:
                print(names[i], "performed better than", names[j])
            elif averages[j] > averages[i]:
                print(names[j], "performed better than", names[i])
            else:
                print(names[i], "and", names[j], "have equal averages")

    # Display class summary
    print("\n===== Class Summary =====")
    print("Total Students:", total_students)
    print("Class Average:", round(class_average, 2))
    print("Highest Average:", highest_average)
    print("Lowest Average:", lowest_average)
    print("Passing Students:", passing_students)
    print("Failing Students:", failing_students)
    print("Students Above Class Average:", above_average)

else:
    print("No student records entered.")
