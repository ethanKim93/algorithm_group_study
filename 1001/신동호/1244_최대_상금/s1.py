import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, list(str(N))))
    ori = list(map(int, list(str(N))))

    for i in range(len(num)-1):
        maxI = i
        for j in range(i+1, len(num)):
            if num[maxI] < num[j]:
                maxI = j
        num[maxI], num[i] = num[i], num[maxI]

    print(ori, num)
    for i in range(len(num)):
        if num[i] == ori[i]:
            print('0', end='')
        else:
            print('1', end='')
    print()

    # for x in range(M):
    #     flag = 0
    #     for i in range(len(num)-1):
    #         maxI = i
    #         for j in range(len(num)-1, i, -1):
    #             if num[maxI] < num[j]:
    #                 maxI = j
    #                 flag = 1
    #         if flag:
    #             print('swap')
    #             print(i, maxI)
    #             num[i], num[maxI] = num[maxI], num[i]
    #             break
    # print(num)

