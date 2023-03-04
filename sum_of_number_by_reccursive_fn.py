def SUM(n):
    if n==0:
        return 0
    return n+SUM(n-1)
num=int(input('\nEnter a Number : '))
print(f'Sum of All Natural Numbers till {num} is {SUM(num)}')