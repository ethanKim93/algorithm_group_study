import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    opt_str = input()

    stack = []
    num_lst = []

    icp = {'*': 2, '+': 1, '(': 3}  # 넣을때
    isp = {'*': 2, '+': 1, '(': 0}  # 스택안

    for i in range(N):
        if opt_str[i].isdigit():
            num_lst.append(opt_str[i])

        else:
            if not stack:
                stack.append(opt_str[i])
                continue

            elif stack:
                if opt_str[i] == ')':
                    while stack[-1] != '(':
                        num_lst.append(stack.pop())
                    stack.pop()

                elif icp[opt_str[i]] > isp[stack[-1]]:
                    stack.append(opt_str[i])

                else:
                    while icp[opt_str[i]] <= isp[stack[-1]]:
                        num_lst.append(stack.pop())
                    stack.append(opt_str[i])

    for i in range(len(num_lst)):
        if num_lst[i].isdigit():
            stack.append(num_lst[i])

        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())

            if num_lst[i] == "+":
                result = num1 + num2
            elif num_lst[i] == "*":
                result = num1 * num2

            stack.append(str(result))

    print('#{} {}'.format(tc, stack[0]))
