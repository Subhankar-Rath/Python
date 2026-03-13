user=input("enter the username: ")
password=input("enter the password: ")
if(user=="admin" and password=="123"):
    print("you are successfully log in")
else:
    if(user!="admin"):
        print("wrong username")
    else:
        print("wrong password")