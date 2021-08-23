import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    t = input()

    i = 0
    start = 0
    count = 0
    while i < len(t):
        if t[i] == '(' and t[i+1] == ')':
            count += start
            i += 2
        elif t[i] == '(':
            start += 1
            i += 1
        elif t[i-1] != '(' and t[i] == ')':
            start -= 1
            count += 1
            i += 1

    print('#{} {}'.format(tc, count))







    for i in range(len(t)):
        if i == '(' and i+i == ')':
            count += start

