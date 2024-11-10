side1=float(input("Enter 1st side of triangle:"))
side2=float(input("Enter 2nd side of triangle:"))
side3=float(input("Enter 3rd side of triangle:"))

if side1+side2>side3 and side1+side3>side2 and side3+side2>side1:
 if side1==side2==side3:
    print("This is equilivent triangle.")
 elif side1==side2 or side1==side3 or side2==side3:
    print("This is isosceles triangle.")
 else:
   print("This is scalene triangle")
else:
  print("its not valid triangle sides")