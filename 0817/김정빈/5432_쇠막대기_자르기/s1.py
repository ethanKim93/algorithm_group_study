import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    iron = input()
    cut = iron.replace('()','*')
    op = 0
    tot = 0
    for i in cut:
        if i == '(':
            op += 1
            tot += 1
        elif i == ')':
            op -= 1
        else: #레이저만날경우
            tot += op

    print('#{} {}'.format(tc, tot))