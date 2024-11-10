temp=int(input("Enter temperature in celcius:"))

if temp <=0:
    print(f"{temp}*c is freezing temperature")
elif temp <=30 :
    print(f"{temp}*c is moderate temperature")
else:
    print(f"{temp}*c is hot temperature")