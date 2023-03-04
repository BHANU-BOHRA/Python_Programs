s1=int(input("\nEnter the Marks of Subject 1 : "))
s2=int(input("\nEnter the Marks of Subject 2 : "))
s3=int(input("\nEnter the Marks of Subject 3 : "))
s4=int(input("\nEnter the Marks of Subject 4 : "))
s5=int(input("\nEnter the Marks of Subject 5 : "))
if(s1<33 or s2<33 or s3<33 or s4<33 or s5<33)or((s1+s2+s3+s4+s5)/5<40):
    print("\nStudent is 'FAIL'")
else:
    print("\nStudent is 'PASS'") 