num=int(input("enter a number:"))
largestdig=0
smallestdig=9
while num>0:
    rem=num%10
    if smallestdig>rem:
        smallestdig=rem
    if largestdig<rem:
        largestdig=rem
    num=num//10
print("largest digit is:",largestdig)
print("smallest digit is:",smallestdig)
sum=largestdig+smallestdig
difference=smallestdig-largestdig
print("sum is: ",sum)
print("difference is: ",difference)
