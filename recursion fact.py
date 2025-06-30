def factorial(n):
    if n==1:
        return 1
    else:
        return (n*factorial(n-1))
num=int(input("enter a number:"))
if num<0:
    print("factorial doesnt exist for negative numbers")
elif num==0:
    print("factorial of 0 is 1")
else:
    factorial=factorial(num)
    print("factorial of",num,"is:",factorial)
