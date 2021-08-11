import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    dump = int(input())
    maps = list(map(int, input().split()))
    cnt = 0

    # 최초 Dump 전 정렬
    for i in range(99, -1, -1):
        for x in range(i):
            if maps[x] > maps[x+1]:
                maps[x], maps[x+1] = maps[x+1], maps[x]

    while True:
        # Dump
        maps[-1] -= 1
        maps[0] += 1
        cnt += 1

        # Dump 후 정렬
        for i in range(99, -1, -1):
            for x in range(i):
                if maps[x] > maps[x+1]:
                    maps[x], maps[x+1] = maps[x+1], maps[x]

        # 평탄화 작업이 완료 되었거나, dump 제한 횟수 도달시
        if maps[-1] - maps[0] <= 1 or cnt == dump:
            break

    print("#{} {}".format(tc, maps[-1]-maps[0]))


# 너무 무식한 코드 같습니다ㅠ 다른 방법이 궁금합니다.