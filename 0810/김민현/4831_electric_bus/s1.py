import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    KNM = list(map(int,input().split()))
    K = KNM[0]
    N = KNM[1]
    M = KNM[2]
    M_list = list(map(int,input().split()))


    sts = 0 # 현재 위치
    cnt = 0 # 충전회수

    while sts <= 10:
        if sts + N > 10:
            break
        flag = 0
        for i in range(M-1):
            if sts > M_list[i]: #현재 위치보다 뒤에 있는 정류장은 넘어감
                continue
            elif N > M_list[i+1] - sts: #다음정거장까지 갈 수 있는 경우
                flag = 1

            if flag == 1:
                if K > M_list[i+1] - sts:
                    continue
                else:
                    sts = M_list[i]
                    break
            else: #다음정거장 까지 못갈 경우
                cnt = 0
                break
        if flag == 1:
            cnt += 1

    print('#{0} {1}'.format(tc,cnt))