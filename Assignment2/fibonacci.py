#Program to caluclate Fibonnaci series.
class Fibonnaci:
	def fib(n):
		if (n==0 or n==1):
			return n 
		else:
			return Fibonnaci.fib(n-1)+ Fibonnaci.fib(n-2)
	
	def main(self):
		count = 0
		print("Enter the number of outcomes")
		count = int(input())
		print("The", count, "th fibonacci number is :")
		print(self.fib(count))
		
#calling main function in class fibonnaci		
#if __name__=='__name__':
print("Calling main")
a = Fibonnaci
a.main()
