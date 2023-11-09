def element_check(lst,element):
      if element in lst:
            print("Present")
      else:
            print("Not present")
list = input("Enter the list : ").split()
print(element_check(list,'h'))