dict={
    'thali':'plate',
    'dabba':'box',
    'kurshi':'chair',
    'tasveer':'photo'
}
print("\nOptions are :",dict.keys())
a=input("\nEnter the Hindi Word : ")
print('\nThe Meaning of the word in English is :',dict.get(a))