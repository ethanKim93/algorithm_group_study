import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    Nlist = [0] * 5
    factoList = [2, 3, 5, 7, 11]
    for i in range(len(factoList)):
        while 1:
            if N % factoList[i] is 0:
                Nlist[i] += 1
                N //= factoList[i]
            else:
                break

    print('#{} {} {} {} {} {}'.format(tc, Nlist[0], Nlist[1], Nlist[2], Nlist[3], Nlist[4]))