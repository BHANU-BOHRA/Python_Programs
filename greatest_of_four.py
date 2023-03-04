n1=int(input("\nEnter Number 1 : "))
n2=int(input("\nEnter Number 2 : "))
n3=int(input("\nEnter Number 3 : "))
n4=int(input("\nEnter Number 4 : "))
if n1>n2:
    f1=n1
else:
    f1=n2
if n3>n4:
    f2=n3
else:
    f2=n4
if f1>f2:
    print(str(f1)+" is Greatest of Four")
else:
    print(str(f2)+" is Greatest of Four")