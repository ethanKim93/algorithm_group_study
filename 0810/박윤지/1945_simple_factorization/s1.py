import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 5
    num_list = [2, 3, 5, 7, 11]
    for idx in range(4, -1, -1):
        while N % num_list[idx] == 0:
            cnt[idx] += 1
            N /= num_list[idx]
    print('#{} {} {} {} {} {}'.format(tc, cnt[0], cnt[1], cnt[2], cnt[3], cnt[4]))
