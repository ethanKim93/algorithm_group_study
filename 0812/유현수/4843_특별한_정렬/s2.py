# 5팀 최종본

import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for case in range(T):
    N = int(input())
    li = list(map(int, input().split()))

    for i in range(10):                            # 선택정렬
        for j in range(i + 1, N):
            if i % 2:                              # index가 홀수라면
                if li[i] > li[j]:                  # 최소값으로 정렬
                    li[i], li[j] = li[j], li[i]
            else:                                  # index가 짝수라면
                if li[i] < li[j]:                  # 최대값으로 정렬
                    li[i], li[j] = li[j], li[i]

    print("#{}".format(case + 1), end=" ")
    for k in range(10):
        print(li[k], end=" ")
    print()