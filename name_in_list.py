l=['Bhanu','Divya','Megha','Ankit','Neeraj','Aditya','Rahul','Anshu']
name=input("\nEnter your Name : ")
name=name.capitalize()
if name in l:
    print(name + " is Present in the List.")
else:
    print(name + " is not Present in the List.")