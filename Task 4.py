values = [25, 15, 35, 15, 45, 25]
print("Original list:", values)

print("Number of 15s:", values.count(15))
print("Position of 45:", values.index(45))

values.reverse()
print("After reverse:", values)

values.sort()
print("After sort:", values)
