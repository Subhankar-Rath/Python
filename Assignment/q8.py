m=float(input("enter the number"))
operator=input("enter the operator(+,-,*,/)")
n=float(input("enter the number"))

match operator:
    case "+":
        print("result:",n+m)
    case "-":
        print("result",m-n)
    case "*":
        print("result",m*n)
    case "/":
        if(n==0):
            print("invalid result")
        else:
            print("result",m/n)
    case _:
        print("Invalid result")
        