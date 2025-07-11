class student:
    stid=12
    stnm="abhi"

    def getdata(self):
        print("this is student class")

    def getsum(self,a,b):
        print("sum:",a+b)

st=student() #object of class
print("ID:", st.stid)
print("name:", st.stnm)