#Program to print a pattern
class Pattern:
  def main():
    n_rows = 0
    print("Enter the no of rows")
    n_rows=int(input())
    
    for i in range(1,n_rows):
      strng = a.p_aster(i)+ a.p_dlr(i)
      print(strng)
  
  def p_aster(row):
    return(row*'*')
  
  def p_dlr(row):
    return((row+row-1)*'$')
      
a = Pattern
a.main()

b = Pattern
b.main()


# class Pattern:
#   def main(self):
#     n_rows = 5
#     for i in range(1,n_rows):
#       strng = Pattern.p_aster(i)+Pattern.p_dlr(i)
#       print(strng)
#   
#   def p_aster(row):
#     return(row*'*')
#   
#   def p_dlr(row):
#     return((row+row-1)*'$')
#       
# a = Pattern()
# a.main()
