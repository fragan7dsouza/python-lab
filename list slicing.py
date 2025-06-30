a=list(input("enter a list: "))
print(a)
for i in range(1,len(a),1):
    print(a[i:]+a[:i])
