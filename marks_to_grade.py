marks=int(input("\nEnter your marks : "))
if marks<0 or marks>100:
    print("\nImproper Input!")
elif marks>=90:
    print("\nYour Grade is 'Ex'")
elif marks>=80:
    print("\nYour Grade is 'A'")
elif marks>=70:
    print("\nYour Grade is 'B'")
elif marks>=60:
    print("\nYour Grade is 'C'")
elif marks>=50:
    print("\nYour Grade is 'D'")
else:
    print("\nYour Grade is 'F'")