
import module1
from module1 import *

lst1 = input("Enter the list : ").split()

print(module1.reverse_list(lst1))
print(module1.remove_item(lst1,5))
print(module1.append_item(lst1,7))