num=int(input("Enter number:"))
i=1
count=0
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1
if count==2:
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")