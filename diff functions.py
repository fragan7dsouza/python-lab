str=input("enter a string: ")
print("length of the string is:",len(str))
upperstr=str.upper()

containspy="python" in str.lower()
print("contains python?",containspy)

replacedstr=str.lower().replace("python","py3")
print("replaced string is: ",replacedstr)

wordlist=str.split()
print("the string after making a list:",wordlist)

joinedstr="-".join(wordlist)
print("string post joining:",joinedstr)

reversedstr=str[::-1]
print("reversed string is:",reversedstr)
