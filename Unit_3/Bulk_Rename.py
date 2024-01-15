import os
def main():
   i = 1
   path = "E:/Rishith/Anime/DUHUSIAOSKQOIDJOWDFUWHDUHWOD/"               # path of the folder(but instead of \(up) use /(down))
   for filename in os.listdir(path):
      my_dest = "The Battle of Unato - "+str(i)+".mkv"
      my_src = path + filename
      my_dest = path + my_dest
      os.rename(my_src, my_dest)
      i+=1

if __name__ == "__main__":
   main()