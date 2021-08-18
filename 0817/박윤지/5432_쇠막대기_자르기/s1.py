import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    work = input()
    stick = 0
    result = 0
    workStar = work.replace('()', '*')

    for s in workStar:
        if s == '(':
            stick += 1
        elif s == '*':
            result += stick
        elif s == ')':
            stick -= 1
            result += 1

    print('#{} {}'.format(tc, result))

