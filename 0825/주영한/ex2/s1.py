
# 마이츄의 총 갯수
mychew = 20

# 방문횟수를 나타내는 리스트
visited = [0]

# 마이츄를 가지고 있는 갯수를 나타내는 리스트
has_mychew = [0]

# 초기 큐에는 1이 들어가 있고, 새로 들어갈 인원은 2이다.
queue = [1]
new_one = 2

# 마이츄가 다 떨어질 때 까지 반복한다.
while mychew > 0:
    print(queue)

    # visited, has_mychew에 사용될 인덱스와 사람의 번호를 일치하기 위하여 1을 빼주었다.
    temp = queue.pop(0) - 1

    # 방문 횟수를 하나 증가시키고, 방문 횟수 만큼의 마이츄를 가져간다.
    visited[temp] += 1
    has_mychew[temp] += visited[temp]

    # 가져간 만큼 총 마이츄 갯수에서 빼준다.
    mychew -= visited[temp]

    # 해당 인원을 바로 큐에 추가해준다.
    queue.append(temp + 1)

    # 그 다음 번호의 사람을 큐에 추가해준다.
    queue.append(new_one)

    # 인덱스 에러를 막기위하여 visited와 has_mychew에 새로 들어오는 사람의 정보가 저장될 공간을 마련한다.
    visited.append(0)
    has_mychew.append(0)

    # 새로 들어올 사람을 최신화 한다.
    new_one += 1


    if mychew < 0:
        print("{} get {} mychew(has to get {} more)".format(temp + 1, visited[temp] + mychew, -mychew))
    else:
        print("{} get {} mychew".format(temp + 1, visited[temp]))
