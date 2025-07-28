#Print sum of N numbers
print ("Sum of N Numbers")
n =0
sum1 =0
arraynum = []
n = int(input("Enter total numbers: "))

for i in range(0,n): 
	arraynum.append(int(input("Enter the numbers: ")))
	print ("The " , i,"th number is" ,arraynum[i])
	sum1= sum1 +arraynum[i]

print ("Sum of N numbers",arraynum, " is ", sum1)