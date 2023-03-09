for i in range(2,21):
    with open(f"Tables/Multiplication_Table_of_{i}.txt",'w') as f:
        f.write(f' * * * Multiplication Table of {i} * * *\n')
        for j in range(1,11):
            f.write(f"\n  {i} x {j:02} = {i*j:3}")