import sys
sys.stdin = open("sample_input.txt")


def check_corridor(room):
    room[0] = room[0] if room[0] % 2 else room[0] - 1
    room[1] = room[1] + 1 if room[1] % 2 else room[1]


def runaway(rooms, dones, rests, cnt):
    if len(rooms) == 0:
        return cnt
    std_room = rooms.pop(0)
    check_corridor(std_room)
    dones.append(std_room)
    while rooms:
        flag = True
        temp_room = rooms.pop(0)
        check_corridor(temp_room)
        for done in dones:
            if temp_room[0] > done[1] or temp_room[1] < done[0]:
                continue
            else:
                rests.append(temp_room)
                flag = False
                break
        if flag:
            dones.append(temp_room)
    cnt += 1
    return runaway(rests, [], [], cnt)


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 이동하는 경우에 대해 정렬하여 처리
    rooms = [sorted(list(map(int, input().split()))) for _ in range(N)]
    cnt = runaway(rooms, [], [], 0)
    print("#{} {}".format(tc, cnt))