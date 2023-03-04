def table(n,i=10):
    if i==0:
        return
    table(n,i-1)
    print(f'{n} x {i} = {n*i}')
n=int(input('\nEnter a Number : '))
table(n)