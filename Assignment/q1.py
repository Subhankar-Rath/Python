salary=int(input("enter your salary:"))
if salary==30000:
    rate=0.05
elif salary>=70000:
    rate=0.15
else:
    rate=0.25

final_salary=salary*rate
print("tax rate=",rate*100)
print("salary=",salary*rate)