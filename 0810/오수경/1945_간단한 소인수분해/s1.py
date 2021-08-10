import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    list_a = [2, 3, 5, 7, 11]
    list_up = []

    for a in list_a:
        remain = 0
        cnt = 0
        while remain == 0:
            if N % a != 0:
                break
            else:
                N = N//a
                remain = N%a
                cnt += 1

        list_up.append(cnt)


    # print('#{} {} {} {} {} {}'.format(tc,list_up[0], list_up[1], list_up[2], list_up[3], list_up[4]))
