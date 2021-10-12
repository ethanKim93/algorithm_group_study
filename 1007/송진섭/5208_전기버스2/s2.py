import sys
sys.stdin = open('sample_input.txt')

def bus(idx):
    global result, cnt

    if result <= cnt:       # 가지치기
        return

    if idx >= len(li):
        if result > cnt:
            result = cnt
        return

    for i in range(idx + li[idx], idx, -1): # 뒤에서부터 확인
        cnt += 1
        bus(i)
        cnt -= 1    # 원복


T = int(input())

for tc in range(1, T+1):
    li = list(map(int, input().split()))

    cnt = 0
    result = 999999999
    bus(1)
    print('#{} {}'.format(tc,result-1))