import sys
sys.stdin = open("input.txt")
for _ in range(10):
    tc = int(input())
    arr2d = [list(map(int, input().split())) for _ in range(100)]

    tot_sum = [] # 행의 합, 열의 합, 크로스 합들을 모으는 리스트
    sumij = sumij_cross = 0 # 크로스 합은 한 arr2d에 하나씩이므로 반복문 밖에서 초기화
    for i in range(len(arr2d)):
        sumj = sumi = 0 # 행과 열의 합은 한라인에 하나씩 나옴

        for j in range(len(arr2d)):
            sumj += arr2d[i][j]
            sumi += arr2d[j][i]
            if i == j:
                sumij += arr2d[i][j]
            if i+j == len(arr2d)-1:
                sumij_cross += arr2d[i][j]

        tot_sum.append(sumj)
        tot_sum.append(sumi)

    tot_sum.extend([sumij, sumij_cross])

    max_tot = 0
    for tot in tot_sum:
        if tot > max_tot:
            max_tot = tot

    print('#{} {}'.format(tc, max_tot))
