import sys
sys.stdin = open("input.txt")
#
# T = int(input())
# for tc in range(1,T+1):
#     s = input()
#     stack = []
#     for i in s:
#         if i == '{' or i == '(':
#             stack.append(i)
#         elif i == '}':
#             if '{' != stack[-1] or len(stack)==0:
#                 s.append('0')
#                 break
#             elif stack[-1]=='{':
#                 stack.pop(-1)
#         elif i == ')':
#             if '(' != stack[-1] or len(stack) == 0:
#                 s.append('0')
#                 break
#             elif stack[-1] == '(':
#                 stack.pop(-1)
#     if stack:
#         print('#{} {}'.format(tc, 0))
#     else:
#         print('#{} {}'.format(tc, 1))
T = int(input())

for tc in range(1, T+1):
    text = input()
    stack = []

    for i in text:
        if i =='(' or i =='{':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)

    result = 0 if stack else 1
    print('#{} {}'.format(tc, result))
