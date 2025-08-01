##################################################
#Complete a function that returns a list containing all the mismatched words (case sensitive) between two given input strings 
# For example:
# - string 1: "Firstly this is the first string" 
# - string 2: "Next is the second string" # 
# # - output : ['Firstly', 'this', 'first', 'Next', 'second'].
##################################################

def mismatched_strings(string1, string2):
    string1_list = string1.split()
    string2_list = string2.split()
    mismatched_strings = []
    for word in string1_list:
        if word not in string2_list:
            mismatched_strings.append(word)
    for word in string2_list:
        if word not in string1_list:
            mismatched_strings.append(word)
    return mismatched_strings

if __name__ == "__main__":
    str1 = "Firstly this is the first string"
    str2 = "Next is the second string"
    print(mismatched_strings(str1, str2))  # Expected: ['Firstly', 'this', 'first', 'Next', 'second']

    str3 = "Hello World"
    str4 = "Hello there"
    print(mismatched_strings(str3, str4))  # Expected: ['World', 'there']

    str5 = "Python is great"
    str6 = "Python is great"
    print(mismatched_strings(str5, str6))  # Expected: []

    str7 = ""
    str8 = "Empty string"
    print(mismatched_strings(str7, str8))  # Expected: ['Empty', 'string']

    str9 = "Case Sensitive"
    str10 = "case sensitive"
    print(mismatched_strings(str9, str10))  # Expected: ['Case', 'Sensitive', 'case', 'sensitive']