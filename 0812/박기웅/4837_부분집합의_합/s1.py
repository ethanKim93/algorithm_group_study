import sys
sys.stdin = open("sample_input.txt")

for tc in range(1,int(input())+1):
    N, K = map(int, input().split())
    A = range(1, 13) #1 ~ 12까지 원소를 가진 range 정의
    tot_cnt = 0 #원소의 합이 K 인 부분집합의 개수를 세주는 변수 초기화
    bin_list = []# 부분집합의 개수가 N인 이진수의 리스트
    for i in range(1,13):
        bin_list.append((2**N-1)<<i)
    print(bin_list)

    for i in range(1, 1<<12):
        cnt = part_sum = 0
        for j in range(12):
            if i & (1<<j): # i의 j번째 비트가 1인지 검사
                part_sum += A[j]
                cnt += 1
        if cnt == N and part_sum == K:
            tot_cnt += 1

    # print('#{} {}'.format(tc, tot_cnt))

