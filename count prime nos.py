lower=int(input("enter lower value:"))
upper=int(input("enter upper value:"))
count=0
print("prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            count+=1
            print(num)
if count==0:
    print("no prime nos in given range")
else:
    print("there are",count,"prime nos in given range")
        
