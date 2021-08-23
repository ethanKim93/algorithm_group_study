import sys
sys.stdin = open('input.txt')

def check(num):
    if num == '*':
        return 3
    elif num == '+':
        return 2
    else:
        return 1

def change():
    stack = []
    new_list = []
    for i in range(N):
        num = check(formula[i])
        if num == 3:
            while stack:
                if check(stack[-1]) < num:
                    break
                new_list.append(stack.pop())
            stack.append(formula[i])
        elif num == 2:
            while stack:
                if check(stack[-1]) < num:
                    break
                new_list.append(stack.pop())
            stack.append(formula[i])
        else:
            new_list.append(int(formula[i]))


    while stack:
        new_list.append(stack.pop())
    return new_list

def cal(result):
    stack1 = []
    for i in range(N):
        if result[i] == '*':
            a = stack1.pop()
            b = stack1.pop()
            stack1.append(a * b)
        elif result[i] == '+':
            a = stack1.pop()
            b = stack1.pop()
            stack1.append(a + b)
        else:
            stack1.append(result[i])
    return stack1[0]

for tc in range(1, 11):
    N = int(input())
    formula = input()
    print('#{} {}'.format(tc, cal(change())))

