def kaprekar_constant(n):
    if n=='6174':
        return False
    l=list(n)
    while int(n)<1000:
        l.append('0')
        n*=10
    l.sort()
    min=max=0
    for i in range(0,4):
        max+=int(l[i])*(10**i)
        min+=int(l[i])*(10**(3-i))
    return max-min
num=int(input('Enter a Four Digit Number : '))
if num>9999 or num<1000 or num%1111==0:
    print('Enter a Different Number. ')
else:
    print(f"\nLet's Find how many Attempt it will take to Convert {num} into Kaprekar's Constant.\n\n")
    i=0
    t=str(num)
    while kaprekar_constant(str(t))!=False:
        t=kaprekar_constant(str(t))
        i+=1
        print(f'\nIn Attempt No. {i} We Get {t}')
    print("\nSo,it will take",i,"Attempt to Convert",num,"into Kaprekar Constant")