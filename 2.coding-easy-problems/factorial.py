#Program to calculate factorial of a given number
print("This program calculates the factorial of a given number")
num=int(input("Enter a positive number: "))
print(num)
fact=1
if (num ==0 or num ==1):
	fact=1
else :
	for i in range(num,1,-1):
		#print(fact)
		fact = fact * i
print ("The factorial of the number ", num, " is " , fact)

