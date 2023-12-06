import os
def main():
   i = 1
   path = "D:/Rishith/PES/ui/New folder/"
   for filename in os.listdir(path):
      my_dest = "Chapter "+str(i)+".pdf"
      my_src = path + filename
      my_dest = path + my_dest
      os.rename(my_src, my_dest)
      i+=1

if __name__ == "__main__":
   main()