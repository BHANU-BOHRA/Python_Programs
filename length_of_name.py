name=input("\nEnter You Name : ")
if len(name)<10:
    print("\nYour Name contains less than 10 Characters")
elif len(name)==10:
    print("\nYour Name contains Exactly 10 Characters")
else:
    print("\nYour Name contains more than 10 Characters")