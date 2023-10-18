# File Handeling 2

Fo = open("Big Boy.txt",mode='w')
print("         The truth",file=Fo)
Fo = open("Big Boy.txt",mode='r')
d = Fo.read()
print(d)

print(d.strip())