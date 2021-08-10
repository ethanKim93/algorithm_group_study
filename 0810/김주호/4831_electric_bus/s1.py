import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test in range(T):
    K, N, M = map(int,input().split())
    charge_list = list(map(int,input().split()))

    diff_charge=[]  # 주유소 간의 차이를 저장한 list
    diff_charge.append(charge_list[0])  # 첫번째 주유소까지 가는 거리
    for i in range(M-1): # i번 안에 있는 주유소 사이의 거리
        diff_charge.append(charge_list[i+1]-charge_list[i])
    diff_charge.append(N-charge_list[M-1]) # 마지막 N 정류장까지 남은 거리
    print(diff_charge)

    charge_cnt = 0
    for diff_num in diff_charge:
        if diff_num > K:
            charge_cnt = -1
            break
        else:
            diff_sum = 0
            while K < diff_sum:
                diff_sum += diff_num
            charge_cnt += 1

    print("#{} {}".format(test + 1, charge_cnt))
