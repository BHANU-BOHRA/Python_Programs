n=int(input("\nEnter the Number of Rows : "))
# OLD LOGIC
# for r in range(1,n+1):
#     for c in range(1,n+1):
#         if r==1 or r==n or c==1 or c==n:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print('')

for r in range(n):
    if r==0 or r==n-1:
        print('* '*n)
    else:
        print('*'+' '*(2*n-3)+'*')