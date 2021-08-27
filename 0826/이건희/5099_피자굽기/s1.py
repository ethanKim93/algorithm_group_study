import sys

sys.stdin = open("input.txt")


def check_hwadeok():  # 화덕에 피자가 1개 남았는지 확인
    cnt = 0
    for i in q:  # 화덕을 돌면서
        if i == -1:  # 비어있으면
            cnt += 1  # cnt ++1

    return cnt == hwadeok - 1  # 피자가 1개만 남았는지 return


t = int(input())
for tc in range(1, t + 1):
    hwadeok, pizza = map(int, input().split())  # hwadeok: 화덕의 최대 수용량, pizza: 피자의 갯수
    maps = list(map(int, input().split()))
    for i in range(pizza):
        maps[i] = [i + 1, maps[i]]  # 피자의 고유번호를 피자의 치즈양 앞에 추가

    q = [-1] * hwadeok  # q: 화덕, -1: 빈 칸

    while True:
        if len(maps) == 0 and check_hwadeok():  # 대기열의 피자가 없고, 피자가 1개만 남았으면 종료
            break

        for i in range(hwadeok):  # 화덕 한 바퀴가 한 싸이클
            if q[i] == -1:  # 꺼냈는데 빈 칸이면,
                if maps:  # 남은 피자가 있으면
                    q[i] = maps.pop(0)  # 줄 서 있는 피자 하나 빼서 칸에 넣기
                    q[i][1] = q[i][1] // 2  # (1) 넣은 피자를 다음 턴에 꺼낼 때, //2만큼 녹아있는 상태로 만나기 위해
            else:  # 꺼냈는데 피자가 있으면,
                if q[i][1] == 0:  # 피자가 완성되었으면
                    if maps:  # 대기하는 피자가 있으면
                        q[i] = maps.pop(0)  # 새로운 피자 넣기
                        q[i][1] = q[i][1] // 2  # (1)
                    else:  # 대기하는 피자가 없으면
                        q[i] = -1  # 빈 칸으로 냅두기

                else:  # 피자가 완성되지 않았으면
                    q[i][1] = q[i][1] // 2  # (1)

            # 남은 피자 2개가 동시에 0개가 될 경우 대비
            if len(maps) == 0 and check_hwadeok():  # 대기열의 피자가 없고, 피자가 1개만 남았으면 종료
                break

    for i in q:  # 화덕을 돌면서
        if i != -1:  # 화덕에 피자가 있는 칸을 찾으면
            ans = i[0]  # 그 칸의 고유번호가 answer

    print("#{} {}".format(tc, ans))
