import sys

sys.stdin = open("input.txt")


T = int(input())
for t in range(1,T+1):
    N = int(input())
    N_list = list(map(int,input().split()))
    N_list = N_list[::-1]
    max_list = N_list[0]
    cnt = 0
    for i in range(1,len(N_list)):
        if max_list > N_list[i]:
            cnt += max_list-N_list[i]
        else:
            max_list = N_list[i]
    print("#{} {}".format(t, cnt))