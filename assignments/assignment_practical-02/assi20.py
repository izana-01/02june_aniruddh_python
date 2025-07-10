#Write a Python program to update a value in a dictionary. 
student = {
    "name": "aniruddh",
    "age": 19,
    "rollno": 21,
    "course": "Computer Science",
    "grade": "B",
}

print("Original dictionary:")
print(student)

student["grade"] = "A"

print("Updated dictionary (after changing grade):")
print(student)