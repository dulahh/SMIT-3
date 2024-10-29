age=int(input("enter your age:"))

if age < 18:
    print("you are a minor citizen")
elif age < 65:
    print("you are a  adult citizen")
else:
    print("you are a senior citizen")