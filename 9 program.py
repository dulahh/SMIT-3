a=float(input("Enter 1st side value if triangle"))
b=float(input("Enter 2nd side value if triangle"))
c=float(input("Enter 3rd side value if triangle"))

if a+b>c and b+c>a and a+c>b:
    print("It is valid triangle")
else:
    print("its not valid triangle")