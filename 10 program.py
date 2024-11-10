char=input("Enter a character:")
char=char.lower()

if char.isalpha():
    if char in 'aeiou':
        print(f"{char} is a vowle")
    else:
        print(f"{char} is a consonant") 
else:
    print("Enter a valid character")       