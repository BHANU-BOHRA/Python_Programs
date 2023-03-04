message=input("\nEnter the Message : ")
if("make a lot of money" in message)or("buy now" in message)or("subscribe this" in message)or("click this" in message):
    print(message + " is a spam message.")
else:
    print(message + " is not a spam message.")