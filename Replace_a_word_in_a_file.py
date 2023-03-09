c=input('Enter the Word You want to Censor in Flie "censor.txt" : ')
with open('censor.txt') as f:
    t=f.read()
if c in t:
    t=t.replace(c,'$#@%*#^!')
with open('censor.txt','w') as f:
    f.write(t)
print(f'"{c}" has been Successfully Censored.')