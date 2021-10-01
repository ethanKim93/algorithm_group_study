'''
< 오답 이유 >
각 순간에 최적해를 선택하는 방식으로 교환을 실행하면
32888 2
와 같은 케이스에서 정답이 나오지 않는다.

이 코드에서는 88823을 출력하지만
정답은 88832다.

DFS로 모든 경우의 수를 확인해야 한다.
'''

import sys
sys.stdin = open('input.txt')


# 교환할 2개의 인덱스 조합을 comb_li에 저장하는 함수
def nC2(n, s, k):
    if k == 2:
        tmp = comb[:]
        comb_li.append(tmp)
    else:
        for i in range(s, n-2+k+1):
            comb[k] = i
            nC2(n, i+1, k+1)


# 인덱스 조합을 돌며 변화하는 금액이 가장 큰 인덱스 조합을 찾아 교환을 실행하는 함수
def exchage(arr, li):
    n = len(li)
    max_idx = 0
    max_val = 0
    for i in range(n):
        val1 = arr[li[i][0]] * (10 ** (len_N - 1 - li[i][0])) + arr[li[i][1]] * (10 ** (len_N - 1 - li[i][1]))
        val2 = arr[li[i][0]] * (10 ** (len_N - 1 - li[i][1])) + arr[li[i][1]] * (10 ** (len_N - 1 - li[i][0]))
        if max_val < val2 - val1:
            max_val = val2 - val1
            max_idx = i
    arr[li[max_idx][0]], arr[li[max_idx][1]] = arr[li[max_idx][1]], arr[li[max_idx][0]]


def get_idx(arr):
    n = len(arr)
    for i in range(n):
        if arr.count(arr[i]) > 1:
            idx1 = i
            for j in range(i+1, n):
                if arr[i] == arr[j]:
                    idx2 = j
                    return idx1, idx2
    else:
        idx1 = arr.index(min(arr))
        idx2 = 0
        for i in range(n):
            if i != idx1 and arr[idx2] > arr[i]:
                idx2 = i
        return idx1, idx2


T = int(input())
for tc in range(1, T+1):
    N, C = input().split()
    N = list(map(int, N))
    C = int(C)
    len_N = len(N)

    # 최댓값 저장
    max_prize = N[:]
    max_prize.sort(reverse=True)

    # 순열 만들기
    comb = [0] * 2
    comb_li = []
    nC2(len_N, 0, 0)

    # 최대 금액과 같거나 교환 횟수를 모두 쓸때까지 교환 실행
    while N != max_prize and C > 0:
        exchage(N, comb_li)
        C -= 1

    # 남은 교환 횟수 처리
    if C % 2:
        i1, i2 = get_idx(N)
        N[i1], N[i2] = N[i2], N[i1]

    ans = [str(num) for num in N]

    print('#{} {}'.format(tc, ''.join(ans)))
