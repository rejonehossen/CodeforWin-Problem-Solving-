a=1
while a:
    a=int(input("Enter a month number= "))
    
    if a==1 or  a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
        print(31)
    elif a==4 or a==6 or a==9 or a==11:
        print(30)
    elif a==2:
        print("28 or 20")
    else:
        print("Please enter a valid month number")
    continue