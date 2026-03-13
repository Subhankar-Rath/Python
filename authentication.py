user=input("enter the unsername:")
password = input("enter the password:")
if(user=="admin" and password=="123"):
    print("log in successful")
elif(user!="admin"):
    print("wrong user name")
else:
    print("wrong password")
