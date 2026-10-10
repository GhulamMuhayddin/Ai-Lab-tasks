names = []
averages = []
# Enter student records using while loop
while True:
    name = input("\nEnter student name (-1 to stop): ")

    if name == "-1":
        break

    total = 0

    # Enter marks using for loop
    for i in range(3):
        if i == 0:
            marks = float(input("Enter Programming marks: "))
        elif i == 1:
            marks = float(input("Enter Mathematics marks: "))
        else:
            marks = float(input("Enter AI marks: "))

        total += marks

    average = total / 3

    names.append(name)
    averages.append(average)

    print("Total Marks:", total)
    print("Average Marks:", average)

# Compare every student with every other student
print("\n===== Student Comparisons =====")

for i in range(len(names)):
    for j in range(i + 1, len(names)):
        print(names[i], "Average:", averages[i])
        print(names[j], "Average:", averages[j])

        if averages[i] > averages[j]:
            print(names[i], "performed better than", names[j])
        elif averages[j] > averages[i]:
            print(names[j], "performed better than", names[i])
        else:
            print(names[i], "and", names[j], "have equal averages")

        print("----------------------")
