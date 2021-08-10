import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    N_list = [N]*5 # 계산할 값 리스트
    s_list = [2,3,5,7,11] #소수 리스트
    result_list =[0]*5 # 결과값 리스트
    print('#{}'.format(tc),end='')

    for i in range(0,5):
        k = N_list[i]
        while 1:
            if k % s_list[i] == 0: # 소수로 나누어 진다면
                k = k / s_list[i]
                result_list[i] += 1
            else :
                print(' {}'.format(result_list[i]),end='')
                break
    print()
