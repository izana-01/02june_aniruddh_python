"""class student:
    stid=input("enter stid:")
    stnm=input("enter stnm:")

    def getdata(self):
        print("this is student class")

st=student() #object of class
print("ID:", st.stid)
print("name:", st.stnm)"""

class student:
    stid=input("enter stid:")
    stnm=input("enter stnm:")

    def getdata(self):
        print("Student id:", student.stid)
        print("student name:", student.stnm)

st=student()
st.getdata()