import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    cnt = [0, 0]  # A,B
    end = [Pa, Pb]
    for i in range(2):  # A,B
        l = 1
        r = P  # 오른쪽 끝값 = 총 페이지수
        while True:
            c = int((l + r) / 2)
            cnt[i] += 1
            if c == end[i]:
                break
            elif c < end[i]:  # 나눈 값이 목표값보다 작으면
                l = c
            else:  # 나눈 값이 목표값보다 크다면
                r = c

    if cnt[0] == cnt[1]:
        print('#{} 0'.format(tc))
    elif cnt[0] < cnt[1]:
        print('#{} A'.format(tc))
    else:
        print('#{} B'.format(tc))
