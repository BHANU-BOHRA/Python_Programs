import random
def game():
    return random.randint(0,100)
g=game()
with open('hiscore.txt','r') as f:
    score=f.read()
print('\nYour Score Latest Score is',g)
if score=='' or int(score)<g:
    with open('hiscore.txt','w') as f:
        f.write(str(g))
    print('\nHiscore has been Updated.')