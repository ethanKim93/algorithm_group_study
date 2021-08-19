import sys
sys.stdin = open('input.txt')

def check(c_list):
    c_stack = []
    for i in c_list:
        if i == '(':
            c_stack.append(i)
        else:
            if c_stack[-1] == '(':
                c_stack.pop()
            else:
                c_stack.append(i)

    if len(c_stack) == 0:
        return True
    else:
        return False

T = input()
print(check(T))
T = input()
print(check(T))




