# 비트 연산으로 풀어보기
import sys
sys.stdin = open('sample_input.txt')

arr12= []
for i in range(1,13):
    arr12.append(i)
n = len(arr12)

Test_Cases = int(input())

for test in range(Test_Cases):

    subset = []
    for i in range(1, 1 << n):
        arr = []
        for j in range(n):
            if i & (1 << j):
                arr.append(arr12[j])
        subset.append(arr)

    N, K = map(int, input().split())

    result_cnt = 0
    for sub in subset:
        if len(sub) == N:
            sub_sum =0
            for sub_ele in sub:
                sub_sum += sub_ele
            if sub_sum == K:
                result_cnt += 1

    print('#{} {}'.format(test+1, result_cnt))