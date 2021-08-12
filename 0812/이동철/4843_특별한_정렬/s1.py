import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))

    for i in range(len(N_list)-1, 0, -1):
        for j in range(0, i):
            if N_list[j] > N_list[j+1]:
                N_list[j], N_list[j+1] = N_list[j+1], N_list[j]

    sp_list = []
    while N_list:
        if len(sp_list) % 2:
            sp_list.append(min(N_list))
            N_list.remove(min(N_list))
        else:
            sp_list.append(max(N_list))
            N_list.remove(max(N_list))

    print('#{}'.format(tc), end=' ')
    print(*sp_list[0:10])
