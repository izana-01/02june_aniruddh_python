#Write a Python program to separate keys and values from a dictionary using keys() and values() methods. 
student = {
    "name": "aniruddh",
    "age": 19,
    "course": "Computer Science",
    "grade": "A",
}

keylist = list(student.keys())
valuelist = list(student.values())

print("Original Dictionary:")
print(student)

print("Keys:")
print(keylist)

print("Values:")
print(valuelist)