'''
k, l, m, n and d, 
1
2
3
4
12

'''

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
total_not_divisible = 0

for i in range(1, d+1):
    if i % k!=0 and i %l != 0 and i %m !=0 and i%n !=0:
        total_not_divisible +=1
print(d - total_not_divisible)
