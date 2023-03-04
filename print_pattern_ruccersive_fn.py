def pattern(r):
    if r==0:
        return
    print('* '*r)
    pattern(r-1)
n=int(input(']nEnter the Number of Rows : '))
pattern(n)