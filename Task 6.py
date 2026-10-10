#Create a dictionary containing a student's name, age, program, and marks. Display and update selected values.
student = {
    "name": "Hassan",
    "age": 19,
    "program": "BS Artificial Intelligence",
    "marks": 82
}

print("Student Name:", student["name"])
print("Age:", student["age"])
print("Program:", student["program"])
print("Marks:", student["marks"])

student.update({"age": 20, "marks": 88})

print("Updated Student Information:")
print(student)
