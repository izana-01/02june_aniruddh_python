name =(input("enter name :"))
if not name.isalpha():
        print("Error: Name must contain alphabets only.")
    
    
email =(input("enter your email:"))
if not email.islower():
       print ("Error: Email must be lowercase only.")
mobile =int(input("enter mobile no:"))


password = input("Enter your password: ")
cpassword = input("Confirm your password: ")
if password != cpassword:
        print("Error: Passwords do not match.")
else :
    print ("log in successful")






"""
na = (input("your name:") )
print =(na.isalpha())"""