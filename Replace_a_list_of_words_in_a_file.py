curse=['donkey','kaddu','harrami','gareeb']
with open('censor.txt') as f:
    t=f.read()
for c in curse:
    t=t.replace(c,'#*%@$!')
with open('censor.txt','w') as f:
    f.write(t)
print("\nFile has been Successfully Censored.\n")