import sys
sys.stdin = open("input.txt")

for _ in range(1, 11):
    tc = int(input())
    maps = [list(map(int, input().split())) for _ in range(100)]
    temps = [[False]*102 for _ in range(100)] # 지나온 길 확인하는 임시 리스트

    # 사다리 양 옆에 0을 추가
    for i in maps:
        i.insert(0,0)
        i.append(0)

    # 도착점 = c
    for c in range(100):
        if maps[99][c] == 2:
            break

    r = 98

    while True:
        if r == 0: # 처음으로 도달하면 break
            ans = c
            break

        while True:
            if maps[r][c-1] == 1 and not temps[r][c-1]: # 왼쪽에 사다리가 있고 지나온 길이 아니면 좌로 1칸
                temps[r][c] = True
                c -= 1
            elif maps[r][c+1] == 1 and not temps[r][c+1]: # 오른쪽에 사다리가 있고 지나온 길이 아니면 우로 1칸
                temps[r][c] = True
                c += 1
            else:
                break

        r -= 1 # 양 옆에 사다리 없으면 한칸 올라가기

    print("#{} {}".format(tc,ans-1))
