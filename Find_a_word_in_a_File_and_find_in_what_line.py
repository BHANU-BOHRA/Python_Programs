t=True
i=1
with open('log.txt') as f:
    while t:
        t=f.readline()
        if 'python' in t.lower():
            print(f'"Python" is present in File at line {i}')
        i+=1