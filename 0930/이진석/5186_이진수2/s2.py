import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, int(input())+1):
    N = float(input())
    answer = ''
    cnt = 0
    while N:
        N *= 2
        answer += str(int(N))       # 정수부 저장
        N -= int(N)                 # 실수부 갱신
        cnt += 1                    # 비트 자릿수 저장
        if cnt > 12:                # 13자리 이상이면 overflow
            answer = 'overflow'
            break
    print('#{} {}'.format(tc, answer))