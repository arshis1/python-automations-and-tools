#########################
'''B. Pathless
time limit per test1 second
memory limit per test256 megabytes
There is an array a1,a2,…,an
 consisting of values 0
, 1
, and 2
, and an integer s
. It is guaranteed that a1,a2,…,an
 contains at least one 0
, one 1
, and one 2
.

Alice wants to start from index 1
 and perform steps of length 1
 to the right or to the left, and reach index n
 at the end. While Alice moves, she calculates the sum of the values she is visiting, and she wants the sum to be exactly s
.

Formally, Alice wants to find a sequence [i1,i2,…,im]
 of indices, such that:

i1=1
, im=n
.
1≤ij≤n
 for all 1≤j≤m
.
|ij−ij+1|=1
 for all 1≤j<m
.
ai1+ai2+…+aim=s
.
However, Bob wants to rearrange a1,a2,…,an
 to prevent Alice from achieving her target. Determine whether it is possible to rearrange a1,a2,…,an
 such that Alice cannot find her target sequence (even if Alice is smart enough). If it is possible, you also need to output the rearranged array a1,a2,…,an
.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤103
). The description of the test cases follows.

The first line of each test case contains two integers n
 and s
 (3≤n≤50
, 0≤s≤1000
).

The second line of each test case contains n
 integers a1,a2,…,an
 (0≤ai≤2
).

It is guaranteed that a
 contains at least one 0
, one 1
, and one 2
.

Output
For each test case, if it is possible to rearrange a
 such that Alice cannot find her target sequence, output n
 integers — such rearrangement of a
. Otherwise, output −1
 instead.
'''
#########################
#tstcases
t = int(input())
for _ in range(t):
    n,target_sum = map(int, input().split())
    arr_list = list(map(int, input().split()))
    arr_sum = 0
    zero_c = 0
    one_c = 0
    two_c = 0
    for num in arr_list:
        arr_sum += num
        if num ==0:
            zero_c +=1
        elif num ==1:
            one_c +=1
        else:
            two_c +=1
    if arr_sum == target_sum:
        print(-1)
    elif arr_sum +2 <= target_sum:
        print(-1)
    else:
        output = []
        for _ in range(zero_c):
            output.append(0)
        for _ in range(two_c):
            output.append(2)
        for _ in range(one_c):
            output.append(1)
        print(" ".join(map(str, output)))
