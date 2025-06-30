a=[]
num=int(input("enter count of elements:"))
for i in range(num):
    a.insert(i,int(input("enter an element:")))
search=int(input("enter an element to search:"))
flag=0
for i in range(num):
    if a[i]==search:
        flag=1
        print("element found at position",i+1)
        break
if flag==0:
    print("element not found")
else:
    print("search complete")
