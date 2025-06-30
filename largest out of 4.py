a=int(input("enter a number a"))
b=int(input("enter a number b"))
c=int(input("enter a number c"))
d=int(input("enter a number d"))
if (a>=b) and (a>=c) and (a>=d):
    print("a is the largest")
if (b>=a) and (b>=c) and (b>=d):
    print("b is the largest")
if (c>=b) and (c>=a) and (c>=d):
    print("c is the largest")
else:
    print("d is the largest")
