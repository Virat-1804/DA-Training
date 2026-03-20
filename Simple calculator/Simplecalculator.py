#Simple Calculator
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operation =input("Choose operation(+,-,*,/): ")
if operation=="+":
    print("result: ",num1+num2)
elif operation=="-":
    print("result: ",num1-num2)
elif operation=="*":
    print("result: ",num1*num2)
elif operation=="/":
    if num2!=0:
        print("result: ",num1/num2)
    else:
        print("error: division by zero!")
else:
    print("Invalid opeartion!")