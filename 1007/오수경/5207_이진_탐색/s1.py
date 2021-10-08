import sys
sys.stdin = open('sample_input.txt')

def binary_search(l, r, num_idx, left, right):
    global cnt
    m = (l+r)//2
    if m == num_idx:
        cnt += 1
        return

    # 처음
    if left == 0 and right == 0:
        if m+1 <= num_idx:
            binary_search(m + 1, r, num_idx, 0, 1)
        else:
            binary_search(l, m - 1, num_idx, 1, 0)

    # 이전 탐색이 왼쪽
    elif left == 1:
        if m+1 <= num_idx:
            binary_search(m + 1, r, num_idx, 0, 1)
        return

    # 이전 탐색이 오른쪽
    elif right == 1:
        if num_idx < m:
            binary_search(l, m - 1, num_idx, 1, 0)
        return


T = int(input())
for tc in range(1, T+1):
    A_num, B_num = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0

    for b in B:
        if b in A:
            binary_search(0, A_num-1, A.index(b), 0, 0)

    print('#{} {}'.format(tc, cnt))