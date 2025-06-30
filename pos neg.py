num=int(input("enter number of elements:"))
a=[]
neg=[]
pos=[]
for i in range(num):
    element=int(input("enter a number: "))
    a.append(element)
for i in a:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)
print("the list is: ",a)
print("the positive values are: ",pos)
print("the negative values are: ",neg)
