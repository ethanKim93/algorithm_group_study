import sys                    #####답이 안나왔습니다 ㅠㅠ 시도한 것까지
sys.stdin = open('input.txt')  ###제출하겠습니다


for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    #  사다리 첫 행에서 출발점 찾기
    for j in range(100):
        if ladder[0][j] == 1:
            result = j

            i = 0
             # 마지막 행 i = 99에 갈때까지 반복
            while i < 100:
                if j - 1 >= 0 and ladder[i][j - 1] == 1:
                    ladder[i][j] = 0
                    j -= 1
                elif j + 1 < 100 and ladder[i][j + 1] == 1:
                    ladder[i][j] = 0
                    j += 1
                else:
                    ladder[i][j] = 0
                    i += 1

            if ladder[i][j] == 2:
                target = result

    print('#{} {}'.format(tc, target))