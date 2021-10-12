import sys
sys.stdin = open("input.txt")

# 참고코드

def select_worker(cnt, temp_result):
    global N, result, height

    if cnt == N:
        if temp_result >= height and result > temp_result:
            result = temp_result
        return

    if result < temp_result:
        return

    select_worker(cnt + 1, temp_result + workers[cnt])
    select_worker(cnt + 1, temp_result)

for tc in range(1, int(input())+1):
    N, height = map(int, input().split())
    workers = list(map(int, input().split()))
    result = 987654321
    used = [0] * N

    select_worker(0, 0)
    print('#{} {}'.format(tc, result-height))