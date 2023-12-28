class parent():
   def __init__(self):
      print("I'm a Parent")
class child1(parent):
    def __init__(self):
        super().__init__()
        print("I'm the first child.")
class child2(parent):
    def __init__(self):
        print("I'm the second child.")

# family = child1()
# family = child2()
