import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    H = list(map(int, input().split()))

    # 버블정렬 이용해서 돌면서 가장 큰 값, 작은값 찾기
    for k in range(1, N+1):
        for end in range(len(H) - 1, 0, -1):
            for i in range(0, end):
                if H[i] > H[i + 1]:
                    H[i], H[i + 1] = H[i + 1], H[i]

        H[0] += 1
        H[-1] -= 1
    # 제일 작은 값에 1 더해주고 큰 값에 1 빼주면서 평준화 시켜주기
    # 그러나!!! 이 마지막 H[0]과 H[-1]에 1 더하고 -1하면서 끝이남
    # 그러므로 결과값은 앞에서 2번째, 마지막에서 2번째를 빼줘야함!
    print('#{} {}'.format(tc, H[-2] - H[1]))










