with open('log.txt') as f:
    t=f.read()
if 'python' in t.lower():
    print('"python" was Found')
else:
    print('"python was not Found"')