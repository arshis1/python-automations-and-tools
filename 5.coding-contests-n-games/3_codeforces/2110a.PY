def make_fashinable2(arr, arr_len):
    arr.sort()
    i = 0
    j = arr_len -1
    counter = 0
    s = arr[i]
    e = arr[j]
    while i<j:

        if (s+e)%2 ==0:
            return counter
        
        if i!=0:
            if (arr[i] + s) %2 !=0:
                return counter
        if j != arr_len -1:
            if (arr[j] + e ) %2 !=0:
                return counter
        counter +=1
        s = arr[i]
        e = arr[j]
        i += 1
        j -= 1

    return counter





def is_even(num):
    if num%2==0:
        return True
    else:
        return False

def make_fashionable(arr, arr_len):
    arr.sort()
    left = 0
    right = arr_len-1
    count_remove_min = 0
    count_remove_max = 0
    prev_min_flag = prev_max_flag = None

    while left < right:
            min_flag = is_even(arr[left])
            max_flag = is_even(arr[right])
            if min_flag == max_flag:
                return max(count_remove_max, count_remove_min)
            prev_min_flag = min_flag
            prev_max_flag = max_flag
            left +=1
            right -=1

            if min_flag == prev_min_flag:
                count_remove_min +=1
            if max_flag == prev_max_flag:
                count_remove_max +=1
    return max(count_remove_max, count_remove_min)

no_of_test = int(input())
for i in range(no_of_test):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    
    print(make_fashinable2(arr,arr_len))

