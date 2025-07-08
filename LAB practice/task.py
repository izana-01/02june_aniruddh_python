

print("===== User Sign-Up Form =====")

try:
    name =(input("enter name :"))
    if not name.isupper():
        print("Error: Name must contain capital latters only.") 

    email =(input("enter your email:"))
    if not email.islower():
      print ("Error: Email must be lowercase only.")

    mobile =(input("enter mobile no:"))
    if not mobile.isdigit() and not len(mobile) == 10:
      print ("mobile no. only can be 10")  


    

    password = input("Enter your password: ")
    if password.isalnum():
     print ("there must be only alphabet and numbers.")


    cpassword = input("Confirm your password: ")
    if password != cpassword:
        print("Error: Passwords do not match.")
    else :
     print ("password and confirm password both are same.")

except Exception as e:
     print("Error:", e)
