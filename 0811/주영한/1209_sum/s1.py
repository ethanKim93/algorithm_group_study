import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    dummy = int(input())

    num_lists = [0] * 100

    maxV = [0] * 103
    # [오른쪽 아래로 향하는 대각선의 합, 왼쪽 아래로 향하는 대각선의 합, 열에 대한 최댓값, 행에 대한 합들...]
    for i in range(100):

        # i열에 대한 리스트를 입력으로 받는다.
        num_lists[i] = list(map(int, input().split()))

        # 오른쪽 아래로 향하는 대각선의 합을 구하기 위해 각 [i, i]를 maxV[0]에 더해준다.
        maxV[0] += num_lists[i][i]

        # 왼쪽 아래로 향하는 대각선의 합을 구하기 위해 각 [i, 100-i-1]를 maxV[1]에 더해준다.
        maxV[1] += num_lists[i][100 - i - 1]

        temp_row_sum = 0
        for j in range(100):
            temp_num = num_lists[i][j]
            # i번째 열에 해당하는 리스트의 합을 구한다.
            # maxV[3] 부터 maxV[102]까지 i번째 행에 해당하는 리스트의 합을 구하기 위해. [i,j]번째 요소를 mavV[3-j]에 더해준다.
            temp_row_sum += temp_num
            maxV[j+3] += temp_num

            # i번째 열에 해당하는 리스트가 현재까지의 최댓값인지 확인한다.
        if maxV[2] < temp_row_sum:
            maxV[2] = temp_row_sum

    result = 0
    #maxV(각 행의 합, 각 열의 합, 각 대각선의 합) 중 최댓값을 찾는다.
    for i in range(103):
        if result < maxV[i]:
            result = maxV[i]

    print("#{} {}".format(tc, result))