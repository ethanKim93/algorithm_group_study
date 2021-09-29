import sys
sys.stdin = open('input.txt')

priority = {'+': 1, '*': 2}
for tc in range(1, 11):
    N = int(input())
    stack = []
    new_exp = []
    exp = list(input())
    idx = 0
    while idx < N:
        if exp[idx].isdigit():
            new_exp.append(int(exp[idx]))
            idx += 1
        else:
            if stack:
                if priority[stack[-1]] >= priority[exp[idx]]:
                    new_exp.append(stack.pop())
                else:
                    stack.append(exp[idx])
                    idx += 1
            else:
                stack.append(exp[idx])
                idx += 1
    if stack:
        for _ in range(len(stack)):
            new_exp.append(stack.pop())

    new_exp = new_exp[::-1]
    print(new_exp)
    #
    # result = []
    # while new_exp:
    #     if type(new_exp[-1]) == int:
    #         result.append(new_exp.pop())
    #     else:
    #         operator = new_exp.pop()
    #         a = result.pop()
    #         b = result.pop()
    #         if operator == '*':
    #             result.append(a*b)
    #         elif operator == '+':
    #             result.append(a+b)
    # print('#{} {}'.format(tc, result[0]))
