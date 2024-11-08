def linear_search(lst,target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
        else:
            return -1

arr = [1,45,87,67,55,101]
target = 45
ta1= 3
ta2 = 101

linear_search(arr,target)
linear_search(arr,ta1)
linear_search(arr,ta2)