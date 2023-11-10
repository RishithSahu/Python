#                                             GENERATOR
# Used to generate values
# yield and next   are the keywords
# It saves a ton + ton of memory and improves performance
def gen():
    yield 'A'                       # Asking the system to get values
    yield 'B' 
    yield 'C'
    yield 'D'
g = gen()
# print(g)         # this prints the type
# for i in range(100):
#    print("Bru"+'h'*i)
# g = (x for x in range(10000))
# while True:
print(next(g))
print(next(g))