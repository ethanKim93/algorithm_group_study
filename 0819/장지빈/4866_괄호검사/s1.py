import sys
sys.stdin = open('input.txt')

def stack_push(n):
    stack.append(n)
def stack_pop():
    if stack:
        return stack.pop()

T = int(input())
for tc in range(1, T+1):
    t = input()
    stack = []
    flag = True
    ans = 0
    for i in t:
        if i == '[' or i == '(' or i =='{':
            stack_push(i)
        elif i == ']' or i == ')' or i == '}':
            if stack == False:
                flag = False
                break
            elif (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{'):
                stack_pop()
            else:
                flag = False
                break

    if flag and stack == []:
        ans = 1

    print('#{} {}'.format(tc, ans))