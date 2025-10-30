a=float(input("please enter the first number: "))
b=float(input("please enter the second number: "))
def max_of_two(a,b):
    if a>b:
        return a
    else:
        return b
result=max_of_two(a,b)
print("the bigger number is: ",result)