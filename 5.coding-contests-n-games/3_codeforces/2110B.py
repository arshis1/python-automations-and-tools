#unbalance brqackets
def is_balanced(s):
    bracket_dict = {'(': ')', '{': '}', '[': ']'}
    stack = []
    counter = 0
    for i in range(len(s)):
        #print("i: ", i)
        if s[i] in bracket_dict.keys():
            stack.append(s[i])
            counter +=1
        elif s[i] in bracket_dict.values():
            if bracket_dict[stack[0]] == s[i]:
                stack.pop()
                counter -=1
        #print("counter: ", counter)
        #print(stack)
        if i>0 and len(s)-1-i !=0:
            if counter == 0:
                return "YES"
    return "NO"


n = int(input())
for i in range(n):
    s = input()
    print(is_balanced(s))