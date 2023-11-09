# Python program to interchange first and last elements in a list    

list = input("Enter the list : ").split()
def interchange(lst):
      l = len(lst)
      b = lst[l-1]
      a = lst[0]
      lst[l-1]=a
      lst[0] = b
      return lst
print(interchange(list))