a=int(input("Enter first number= "))
b=int(input("Enter second number= "))
c=int(input("Enter third number= "))

if a>b:
    if a>c:
        print(a,"is maximum")
    else:
        print(c,"is maximum")
elif b>c:
    print(b,"is maximum")
else:
    print(c,"is maximum")