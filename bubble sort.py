a=[]
num=int(input("enter number of elements:"))
for i in range(num):
    values=int(input("enter a number: "))
    a.append(values)
for i in range(num-1):
    for j in range(num-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print("list after sorting is:",a)
