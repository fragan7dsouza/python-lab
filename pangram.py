string=input("enter a string: ")
alphabets="abcdefghijklmnopqrstuvwxyz"
flag=0
for char in alphabets:
    if char not in string.lower():
        flag=1
        break
if flag==0:
    print("it is a pangram")
else:
    print("it isnt a pangram")
        
