sen=input("enter a string: ")
sen=sen.lower()
charcount={}
print("total number of characters is:",len(sen))
for char in sen:
    if char.isalnum():
        if char in charcount:
            charcount[char]+=1
        else:
            charcount[char]=1
print(charcount)
