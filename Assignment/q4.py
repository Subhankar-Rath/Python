def count_num(n):
    count=0
    # count must be initialized
    for i in str(n):
        count+=1
    return count
n=int(input("enter the number: "))
print(count_num(n))