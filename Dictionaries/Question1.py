# 1) Create a dictionary with three key-value pairs representing a student's information: name,age , grade.
# Print each key-value pair on a new line.
student = {
    'name': 'Mercy',
    'age': 20,
    'grade': 'A'
}
for key, value in student.items():
    print(f"{key}: {value}")
