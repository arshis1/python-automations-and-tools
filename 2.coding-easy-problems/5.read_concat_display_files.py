#Program to read the files that are given as a command line input and then print the output to one file in the sequence of the input.
class Many_Files:
  x_arr = []
  
  def read_file():
  
    y = input("\nEnter the file name along with the entire directory path: \n")
#     print(y)
#     f = open(y,'r')
#     print(f.read())
    
    with open(y) as f:
      for line in f:
#           print (line)   
          Many_Files.x_arr.append(line)
        
    print("Read another file?\n")
    print("yes\n")
    print("no\n")
    
    z = input()
    if z == 'yes':
      Many_Files.read_file()
    else :
      Many_Files.main()
#       self.print_files()
      
#       l = len(Many_Files.x_arr)
#       print('lenght of array is ',l)
#       
#       for i in range (0,l):
#         print(Many_Files.x_arr[i])

#         with open(Many_Files.x_arr[i]) as f1:
#         f1 = open(Many_Files.x_arr[i])
#           print(f1.read())
    
  def print_files():
    l = len(Many_Files.x_arr)
#     print('lenght of array is ',l)   
    for i in range (0,l):
       print(Many_Files.x_arr[i])
       
  def save_files():
    y = input("\nEnter the entire directory path to save the file:")
    y = y + '\\new_file.txt'
    print(y)
    l = len(Many_Files.x_arr)
    for i in range(0,l):
      with open(y, 'w') as out_file:
        out_file.write('\n'.join(Many_Files.x_arr[i]))            
    
  def main() :
    print("**************************************\n")
    print("Enter the operation you want to perform: \n")
    print("1: Read new file\n")
    print("2: Display the read file\n")
    print("3: Save the read files to one file\n")
    print("4: Exit \n")

    a = int(input())
    if a == 1:
      Many_Files.read_file()
    elif a == 2:
      Many_Files.print_files()
    elif a == 3:
      Many_Files.save_files()
    elif a == 4:
      exit()
    else:
      print("Incorrect input. Enter a valid input\n")
      self.main()
      
a = Many_Files
a.main()
    