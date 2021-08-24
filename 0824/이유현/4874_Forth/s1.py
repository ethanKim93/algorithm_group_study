import sys
sys.stdin = open('sample_input.txt')
#
# T = int(input())
# for tc in range(1, T+1):
#     eq = list(input().split())
#
#     stk1 = []
#
#     for i in range(len(eq)):
#         if eq[i] == '+':
#             if len(stk1) < 2:
#                 ans = 'error'
#                 break
#             else:
#                 num1 = stk1.pop()
#                 num2 = stk1.pop()
#                 stk1.append(num2+num1)
#         elif eq[i] == '-':
#             if len(stk1) < 2:
#                 ans = 'error'
#                 break
#             else:
#                 num1 = stk1.pop()
#                 num2 = stk1.pop()
#                 stk1.append(num2-num1)
#         elif eq[i] == '*':
#             if len(stk1) < 2:
#                 ans = 'error'
#                 break
#             else:
#                 num1 = stk1.pop()
#                 num2 = stk1.pop()
#                 stk1.append(num2*num1)
#         elif eq[i] == '/':
#             if len(stk1) < 2:
#                 ans = 'error'
#                 break
#             else:
#                 num1 = stk1.pop()
#                 num2 = stk1.pop()
#                 stk1.append(int(num2/num1))
#         elif eq[i] == '.':
#             if len(stk1) == 1:
#                 ans = stk1.pop()
#             else:
#                 ans = 'error'
#         else:
#             stk1.append(int(eq[i]))
#
#     print('#{} {}'.format(tc, ans))

# try - except 에러처리
T = int(input())
for tc in range(1, T+1):
    eq = list(input().split())

    stk1 = []

    for i in range(len(eq)):
        try:
            if eq[i] == '+':
                num1 = stk1.pop()
                num2 = stk1.pop()
                stk1.append(num2+num1)
            elif eq[i] == '-':
                num1 = stk1.pop()
                num2 = stk1.pop()
                stk1.append(num2-num1)
            elif eq[i] == '*':
                num1 = stk1.pop()
                num2 = stk1.pop()
                stk1.append(num2*num1)
            elif eq[i] == '/':
                num1 = stk1.pop()
                num2 = stk1.pop()
                stk1.append(int(num2/num1))
            elif eq[i] == '.':
                if len(stk1) == 1:
                    ans = stk1.pop()
                else:
                    ans = 'error'
            else:
                stk1.append(int(eq[i]))
        except IndexError:
            ans = 'error'
            break

    print('#{} {}'.format(tc, ans))







