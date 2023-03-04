def Remove_strip(s,w):
    ns=s.replace(w,'')
    return ns.strip()
string=input("\nEnter a String : ")
word=input("\nEnter the word to remove : ")
print(f"\nString After Removing {word} : {Remove_strip(string,word)}")
