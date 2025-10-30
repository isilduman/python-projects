#Simple Console Calculator
print("select the operation you want to perform")
print("1.Addition(+)")
print("2.Subtraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")
choice=input("choose an operation(+,-,*,/): ")
num1=float(input("please enter the first number: "))
num2=float(input("please enter the second number: "))
if choice=="+":
    print("result: ", num1+num2)
elif choice=="-":
    print("result:", num1-num2)
elif choice=="*":
    print("result:",num1*num2)
elif choice=="/":
    if num2 !=0:
        print("result:",num1/num2)
    print("Error: Cannot divide by zero!")
else:
    print("Invalid operation selected!") 