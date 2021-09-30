def checking(i,x):
    global result
    start = 1
    rflag = False
    result = 0
    while 56 * start < len(maps2[i]):
        if x - 56 * start <= 0 or start >= 10:  # 맵의 범위를 벗어났을 경우 실행 안함
            return False

        check = maps2[i][x - 56 * start + 1:x + 1]  # 56개씩 잘라서

        flag = check[0]
        if flag == "1":  # 처음이 0이 아니면 규칙이 성립할 수 없음 -> 실행 안함
            start += 1
            continue

        cnt = 0
        check_list = []
        for y in range(56*start):  # 56*start개의 숫자를 돌면서
            if flag == check[y]:  # 현재 cnt하고 있는 숫자와 같으면
                cnt += 1  # cnt += 1
            else:  # 그렇지 않으면
                check_list.append(cnt)  # 지금까지 세줬던 cnt 넣어주고
                cnt = 1  # 리셋해서
                flag = check[y]  # 기준 바꿔주고 탐색
        check_list.append(cnt)  # check_list에 마지막 남은 cnt 추가

        rules2 = []
        for a in range(10):
            temps = []
            for b in range(4):
                temps.append(rules[a][b]*start)
            rules2.append(temps)

        ans_list = []  # 일치하는 코드 담아줄 리스트
        for z in range(0, len(check_list), 4):  # 리스트 4개씩 잘라서
            if check_list[z:z + 4] in rules2:  # rule 안에 있으면 넣어주기
                ans_list.append(rules2.index(check_list[z:z + 4]))
            else:
                break

        if len(ans_list) != 8:
            start += 1
            continue

        ans = 0
        for p in range(8):
            if (p+1) % 2 == 0:
                ans += ans_list[p]
            else:
                ans += ans_list[p] * 3

        if ans % 10 == 0:
            for q in ans_list:
                result += int(q)
            rflag = True

        if rflag:
            return result

        else:
            start += 1

    return result

t = int(input())
for tc in range(1, t + 1):
    r, c = map(int, input().strip().split())
    maps = [list(map(lambda x: bin(int(x, 16))[2:], input().strip())) for _ in range(r)]
    maps2 = []
    rules = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2], [1, 2, 3, 1], [1, 1, 1, 4], # 비율 리스트
             [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]
    real_ans = 0
    # 2진수로 된 리스트를 한개 한개 분리하는 리스트 생성 -> maps2
    for i in range(r):
        temps = []
        for x in range(c):
            if maps[i][x] != '0':
                if len(maps[i][x]) != 4: # 앞에 0이 비었을 경우 채워줌
                    maps[i][x] = ['0'] * (4 - len(maps[i][x])) + list(maps[i][x])
                temps.extend(list(maps[i][x]))
            else:
                temps.append(maps[i][x])

        maps2.append(temps)


    flag = False
    for i in range(r - 1, -1, -1): # 끝 행부터
        for x in range(len(maps2[i]) - 1, -1, -1): # 끝 열부터
            if maps2[i][x] == '1':
                a = checking(i,x)
                if a:
                    flag = True
                    real_ans += a
                    break
        if flag:
            break

    if not flag:
        print("#{} {}".format(tc,0))
    else:
        print(("#{} {}".format(tc,real_ans)))

# Fail: Runtime Error