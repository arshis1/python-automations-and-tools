########################################################################################
#Can you do the following without using subquery?: {1,None,1,2,None} --> [1,1,1,2,2] 
# Ensure you take care of case input[None] which means None object.
########################################################################################

def handle_none(input_arr):
    if not input_arr:
        return []
    last_char = None
    for i in range(len(input_arr)):
        if i ==0 and input_arr[i] is None:
            continue
        else:
            if input_arr[i] is None:
                input_arr[i] = last_char
            else:
                last_char = input_arr[i]
    if last_char is None:
        return []
    else:
        return input_arr

if __name__ == "__main__":
    arr_1 = [1,None, 1,2, None]
    print(handle_none(arr_1)) #Expected: [1,1,1,2,2]

    arr_2 = [None, None, None]
    print(handle_none(arr_2)) #Expected: []

    arr_3 = [1,2,3,4]
    print(handle_none(arr_3)) #Expected: [1,2,3,4]

    arr_4 = []
    print(handle_none(arr_4)) #Expected:[]

    arr_5 = [None, 1, 2, None, 3, None]
    print(handle_none(arr_5)) #Expected [1,2,2,3,3]