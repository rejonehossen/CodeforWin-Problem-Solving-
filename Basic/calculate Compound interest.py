principle=int(input("Enter principle= "))
time=int(input("Enter time= "))
rate=float(input("Enter rate= "))

conpound_interest=principle* ((1+(rate/100))**time)

print(f"compound compound interest is= {conpound_interest}")
