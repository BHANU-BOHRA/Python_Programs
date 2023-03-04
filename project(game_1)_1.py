import random
def game(p,c):
    if (p=='S' and c==1)or(p=='W' and c==2)or(p=='G' and c==3):
        print("\n\n\t\t\tIT\tIS\tA\tDRAW")
    elif (p=='S' and c==2)or(p=='W' and c==3)or(p=='G' and c==1):
        print("\n\n\t\t\tYOU\tWON !")
    else:
        print("\n\n\t\t\tYOU\tLOSE !")
p=input("\nSanke(s) , Water(w) , Gun(g) ?  : ")
p=p.capitalize()
c=random.randint(1,3)
if p=='S':
    print("\n\t\tYou have Choosen 'Snake' , and")
elif p=='W':
    print("\n\t\tYou have Choosen 'Water' , and")
elif p=='G':
    print("\n\t\tYou have Choosen 'Gun' , and")
else:
    print("\n\t\tInvalid Input!")
    exit()
if c==1:
    print("\n\t\tComputer has Choosen 'Snake'")
elif c==2:
    print("\n\t\tComputer has Choosen 'Water'")
else:
    print("\n\t\tComputer has Choosen 'Gun'")
game(p,c)