n=int(input("\nEnter the Number to Find Factorial : "))
factorial=1
for i in range(2,n+1):
    factorial*=i
print(f"\nFactorial of {n} is {factorial}")