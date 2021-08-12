import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = []    # 각 영역의 파리 숫자를 담을 배열
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(i,i+M):      # 배열의 M * M 만큼의 합
                for l in range(j,j+M):
                    temp += arr[k][l]
            if max_sum < temp:          # 합의 최대 구하기
                max_sum = temp

    print('#{} {}'.format(tc, max_sum))