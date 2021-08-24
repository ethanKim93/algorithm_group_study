import sys
sys.stdin = open("input.txt")


T = 10

for tc in range(1,T+1):
    N = int(input())
    nums = list(input())
    stack = [nums[0]]
    cal = []
    for num in nums[1:]:
        if num.isdigit():
            cal.append(num)
        else:
            if num == '(':
                stack.append(num)
            elif num == ')':
                while stack[-1] != '(':
                    cal.append(stack.pop())
                stack.pop()
            elif num == '*':
                stack.append(num)
            elif num == '+':
                while stack and stack[-1] != '(':
                    cal.append(stack.pop())
                stack.append(num)
    for c in cal:
        if c.isdigit():
            stack.append(c)
        elif len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            if c == '+':
                stack.append(int(a) + int(b))
            elif c == '*':
                stack.append(int(a) * int(b))
    print('#{} {}'.format(tc, stack[0]))







