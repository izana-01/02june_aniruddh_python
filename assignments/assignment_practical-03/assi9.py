#6: Check file cursor position
with open("sample.txt", "r") as f:
    print(f.tell())  # Print current cursor position