###################################
#"Complete a function that returns the number of times a given character occurs in the given string.
# For example:
# - input string = ""mississippi""
# - char = ""s""
#
# - output : 4"
#################################

def count_characters(input_string, target_char):
    count = 0
    for char in input_string:
        if char ==target_char:
            count+=1
    return count

print(count_characters("mississippi", "s"))  # Output: 4