##########################
# Reverse String Inplace #
##########################

def reverse_string_inplace(input_string):
    input_string_list = list(input_string)
    #we need pointers start and end 
    start = 0
    end = len(input_string_list) -1
    output_list = []

    for i in range(end, -1,-1):
        if start > end:
            break
        output_list.append( input_string_list[i])
    output_string = ''.join(output_list)
    return output_string

if __name__ == "__main__":
    input_string = input("Enter a string to reverse: ")
    print(reverse_string_inplace(input_string))
