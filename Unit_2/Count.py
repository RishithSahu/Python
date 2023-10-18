# Strip method
# Count the number of 'trouble' words in a file

Fo = open(r"Big Boy.txt",mode='r')
d= Fo.readlines()
cou = 0
for i in d:
    cou+=i.count("trouble")
print(cou)