x=1
while x:
    a=int(input("Enter first angle= "))
    b=int(input("Enter second angle= "))
    c=int(input("Enter third angle= "))

    if a>0 and b>0 and c>0:

        if a+b+c == 180:
            print("Valid")
        else:
            print("Not Valid")
    else:
        print("Please enter positive integer value")
    continue