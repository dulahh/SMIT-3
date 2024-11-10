num1=float(input("Enter 1st number:"))
num2=float(input("Enter 2nd number:"))
oper=input("Enter an operation (+,-,*,/):")

if oper == '+':
    print(num1+num2)
elif oper == '-':
    print(num1-num2)
elif oper == '*':
    print(num1*num2)
elif oper == '/':
    print(num1/num2)
else:
    print("Enter valid opreration")


