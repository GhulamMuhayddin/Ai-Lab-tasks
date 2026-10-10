while True:
    name = input("\nEnter student name (or -1 to stop): ")

    if name == "-1":
        break

    programming = float(input("Enter Programming marks: "))
    mathematics = float(input("Enter Mathematics marks: "))
    ai = float(input("Enter Artificial Intelligence marks: "))

    total = programming + mathematics + ai
    average = total / 3

    print("\n----- Student Result -----")
    print("Student Name:", name)
    print("Programming Marks:", programming)
    print("Mathematics Marks:", mathematics)
    print("Artificial Intelligence Marks:", ai)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
