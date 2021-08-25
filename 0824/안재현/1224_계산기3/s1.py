import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    my_string = input()
    back = ''
    stack = []
    for i in my_string:
        if i == '(':
            stack.append(i)
        elif i == '*':
            while stack[-1] == '*':
                back += stack.pop()
            stack.append(i)
        elif i == '+':
            while stack[-1] == '+' or stack[-1] == '*':
                back += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                back += stack.pop()
            stack.pop()
        else:
            back += i

    while stack:
        back += stack.pop()
    result = []
    for j in back:
        if j == '+':
            b = result.pop()
            a = result.pop()
            c = int(a) + int(b)
            result.append(c)
        elif j == '*':
            b = result.pop()
            a = result.pop()
            c = int(a) * int(b)
            result.append(c)
        else:
            result.append(int(j))

    print('#{} {}'.format(tc, result[0]))