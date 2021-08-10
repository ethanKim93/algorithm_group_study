import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    NM = list(map(int,input().split()))
    N = NM[0]
    M = NM[1]
    ai = list(map(int,input().split()))

    #구간합 구하기
    sum_list=[]
    for i in range(N-M+1):
        prefix_sum = 0
        for j in range(i,i+M):
            prefix_sum += ai[j]
        sum_list.append(prefix_sum)

    #버블을 이용하여 최대 최소 구하기
    for i in range(len(sum_list)-1,0,-1):
        for j in range(0,i):
            if sum_list[j] > sum_list[j+1]:
                sum_list[j],sum_list[j+1] =sum_list[j+1],sum_list[j]
    #촤대값- 최소값 결과
    result = sum_list[-1] - sum_list[0]

    print('#{0} {1}'.format(tc,result))


