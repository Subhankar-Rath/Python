student = {
    "name": "Subhankar",
    "age": 20,
    "cgpa": 7.2
}

print("Before changing the key:")
print(student)

# Change the key "name" to "student_name"
student["student_name"] = student.pop("name")

print("\nAfter changing the key:")
print(student)