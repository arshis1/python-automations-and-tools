#Program to print a pattern
class Pattern:
  def main(self):
    n_rows = 5
    for i in range(1,n_rows):
      strng = Pattern.p_aster(i)+Pattern.p_dlr(i)
      print(strng)
  
  def p_aster(row):
    return(row*'*')
  
  def p_dlr(row):
    if row == 1:
      return(row*'$')
    else :
      return((row+row-1)*'$')
      
a = Pattern()
a.main()