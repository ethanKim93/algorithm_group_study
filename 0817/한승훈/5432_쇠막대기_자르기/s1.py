import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    model = input()
    stick = cnt = 0
    i = 0
    while i < len(model):
        if model[i] == '(':
            stick += 1
        else:  # ')'일때
            if model[i-1] == '(':  # 레이져인 경우 ()
                stick -= 1
                cnt += stick
            else:  # 막대기 끝부분인 경우
                stick -= 1
                cnt += 1
        i += 1
    print('#{} {}'.format(tc, cnt))


