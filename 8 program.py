word=str(input("enter word:"))
word1=word[-1::-1]
if word==word1:
 print("palindorum:-",word1)
else:
 print("not palindorum:-",word1)