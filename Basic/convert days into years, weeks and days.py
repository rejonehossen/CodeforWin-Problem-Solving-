a=int(input("Enter days= "))


years=(a//365)
weeks=((a%365)//7)
days=(a%365)%7



print(f"{years} years, {weeks} weeks, {days} days")