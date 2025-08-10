#Balacnce Paranthesis


def isBalanced(s):
    stack = []
    openBrackets = "("
    closeBrackets = ")"

    for char in s:
        #print(char)
        #print (stack)
        if char in openBrackets:
            stack.append(char)
        elif char in closeBrackets:
            if len(stack) ==0:
                return "NO"
            else:
                stack.pop()
        else:
            continue
        
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


input_string = input()

print(isBalanced(input_string))