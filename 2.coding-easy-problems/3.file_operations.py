#Program that will read a file and print it on the console.
# class Read:
# 
#   def read_file():
#     print("**********************\n")
#     print("Now reading file\n")
#     f = open(r'''C:\Python31\README.txt''')
#     Read.print_file(f)
#   
#   def print_file(f):
#     print("**********************\n")
#     print("Display the file\n")
#     print(f.read())
#   
#   def main():
#     print("**************************\n")
#     print("Inside main\n")
#     Read.read_file()
#      
# print("Calling main\n")  
# a = Read
# a.main()


class Read:

  def read_file():
    print("**********************\n")
    print("Now reading file\n")
    f = open(r'''C:\Python31\README.txt''')
    Read.print_file(f)
  
  def print_file(f):
    print("**********************\n")
    print("Display the file\n")
    print(f.read())
  
  def main(self):
    print("**************************\n")
    print("Inside main\n")
    Read.read_file()
     
print("Calling main\n")  
a = Read()
a.main()
