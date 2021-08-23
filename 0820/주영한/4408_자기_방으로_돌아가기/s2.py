import sys
sys.stdin = open("sample_input.txt")

def check_corridor(room):
    room[0] = room[0] if room[0] % 2 else room[0] - 1
    room[1] = room[1] + 1 if room[1] % 2 else room[1]
    return room

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    check = [0] * 401
    # 이동하는 경우에 대해 정렬하여 처리
    rooms = [sorted(list(map(int, input().split()))) for _ in range(N)]
    for room in rooms:
        room = check_corridor(room)
        for idx in range(room[0], room[1] + 1) :
            check[idx] += 1
    cnt = 0
    for idx in range(1, 401):
        if check[idx] > cnt:
            cnt = check[idx]

    print("#{} {}".format(tc, cnt))