letter='''Dear <|Name|>,
     You are Selected!
     <|Date|>'''
n=input('\nEnter Your Name : ')
d=input('\nEnter Date : ')
letter=letter.replace('<|Name|>',n)
letter=letter.replace('<|Date|>',d)
print(letter)