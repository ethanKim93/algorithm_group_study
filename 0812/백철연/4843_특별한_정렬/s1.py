
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lis = list(map(int, input().split()))

    for i in range(0, len(lis)-1):
        minindex = i
        for j in range(i+1, (len(lis))):
            if lis[minindex] > lis[j]:
                minindex = j
        lis[i], lis[minindex] = lis[minindex], lis[i]
        # 선택정렬
    result = []

    for i in range(0, len(lis)//2):
        result.append(lis[len(lis) - 1 - i])    # 정렬된 리스트의 맨마지막, 즉 가장 큰값 먼저 추출
        result.append(lis[i])               # 다음으로 가장 작은값 추출

    re = " ".join(map(str, result))
    print('#{} {}'.format(tc, re))




