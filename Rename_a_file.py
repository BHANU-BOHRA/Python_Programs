from os import remove
with open('sample.txt') as f:
    c=f.read()
with open('renamed_by_python.txt','w') as f:
    f.write(c)
remove('sample.txt')