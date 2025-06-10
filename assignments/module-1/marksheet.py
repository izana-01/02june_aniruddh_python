s1 = int(input("s1 marks:"))
s2 = int(input("s2 marks:"))
s3 = int(input("s3 marks:"))
s4 = int(input("s4 marks:"))

total = s1+s2+s3+s4 
print("Total:", total)

pr= total / 4 
print ("PR:", pr)

if pr>=70 :
    print ("dist.")

elif pr>=60 :
   print ("first class")

elif pr>=50 :
    print ("second class")

elif pr>=40:
    print ("bearly pass")

else :
  print("FAIL")