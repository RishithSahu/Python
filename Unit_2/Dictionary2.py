#
dic = {1:'one fellow',2:'two fellow',3:'three fellow',4:'four fellow',5:'five fellow'}

dic.update({6:'six fellow'})
dic['e'] = 'six fellows'
print(dic)
print(len(dic))
print(dic)

wwwcwin={1:'one fellow',2:'two fellow',3:[1,2,3,4,5],4:'four fellow',(5,6):'five fellow'}   # We cannot use mutable things-list,etc.
print(wwwcwin)


d3 = {}
d3.update({1:'one fellow',2:'two fellow',3:'three fellow',4:'four fellow',5:'five fellow'})
d3.setdefault('6')
print(d3)
print(d3.pop('6'))   # popitem() removes some item
print(d3)

#wwwcwin.clear()
#print(wwwcwin)
#del wwwcwin


d4 = {}
d4 = wwwcwin.copy()
print(d4)

d5 = {}
d5 = d4.fromkeys(d4,"New Fellows")
print(d5)