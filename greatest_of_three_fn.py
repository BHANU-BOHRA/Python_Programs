def great_three(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n3:
        return n2
    return n3
x=int(input("\nEnter the Number 1 : "))
y=int(input("\nEnter the Number 2 : "))
z=int(input("\nEnter the Number 3 : "))
print(f"\nGreatest of three is {great_three(x,y,z)}")