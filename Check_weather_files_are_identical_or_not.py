with open('this.txt') as p:
    with open('copy.txt') as q:
        if p.read()==q.read():
            print("\nThey are Identical.")
        else:
            print("\nThey are Not Identical.")