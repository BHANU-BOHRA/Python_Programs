def greet(name='Stranger'):
    print(f"Hello, {name} have a Good Day.")
name=input("\nEnter Your Name : ")
if len(name)<1:
    greet()
else:
    greet(name)
