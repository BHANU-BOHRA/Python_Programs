i=input('\nEnter a Word which You want to Find in "poems.txt" File : ')
with open('poems.txt') as f:
    t=f.read()
if i in t:
    print(f'\n"{i}" is Present in The File.\n')
else:
    print(f'\n"{i}" is not Present in The File.\n')