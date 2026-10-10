#Demonstrate keys(), values(), items(), get(), update(), and pop() using a dictionary.
student = {
    "name": "Hassan",
    "age": 19,
    "program": "BS AI",
    "marks": 82
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Name using get():", student.get("name"))

student.update({"age": 20, "marks": 88})
print("After update():", student)

student.pop("age")
print("After pop():", student)
