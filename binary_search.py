nums=[]
n=int(input("enter number of elements: "))
for i in range(n):
    nums.insert(i,int(input("enter an element: ")))
print("enter number to search:")
search=int(input())
lower=0
upper=n-1
while lower<=upper:
    middle=(lower+upper)//2
    if nums[middle]<search:
        lower=middle+1
    elif nums[middle]==search:
        print("the number found at position: ",middle+1)
        break
    else:
        upper=middle-1
else:
    print("no number found at the position")
