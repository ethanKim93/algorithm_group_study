t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    q = [0] * 1000000
    start = 0
    rear = 0
    q[start] = [n, 0, -1]
    rear += 1
    visited = [0]*1000001

    while start < rear:
        now, cnt, flag = q[start]
        start += 1

        if now == m:
            ans = cnt
            break

        cnt += 1
        if 0 < now * 2 <= 1000000 and not visited[now*2]:
            visited[now * 2] = 1
            q[rear] = [now * 2, cnt, -1]
            rear += 1

        if 0 < now + 1 <= 1000000 and not visited[now+1] and flag != 0:
            visited[now + 1] = 1
            q[rear] = [now + 1, cnt, 1]
            rear += 1

        if 0 < now - 1 <= 1000000 and not visited[now-1] and flag != 1:
            visited[now - 1] = 1
            q[rear] = [now - 1, cnt, 0]
            rear += 1

        if 0 < now - 10 <= 1000000 and not visited[now-10]:
            visited[now - 10] = 1
            q[rear] = [now - 10, cnt, -1]
            rear += 1



    print("#{} {}".format(tc, ans))

# Pass