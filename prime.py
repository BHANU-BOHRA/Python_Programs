n=int(input("\nEnter a Number : "))
p=True
for d in range(2,int(n/2)+1):
    if n%d==0:
        p=False
        break
if p:
    print(f"{n} is a Prime Number.")
else:
    print(f"{n} is not a Prime Number.")