dice = [1, 2, 3, 4, 5, 6]

N, M = map(int, input().split())

# 주사위를 N번 던져서 나올 수 있는 모든 경우
if M == 1:
    for i in dice:
        for j in dice:
            for h in dice:
                print(i, j, h)

# 주사위를 N번 던져서 중복이 되는 경우를 제외하고 나올 수 있는 모든 경우
elif M == 2:
    for i in dice:
        for j in range(i, 7):
            for h in range(j, 7):
                print(i, j, h)

# 주사위를 N번 던져서 모두 다른 수가 나올 수 있는 모든 경우
elif M == 3:
    visited = [0] * 7
    for i in dice:
        if not visited[i]:
            visited[i] = 1
        for j in dice:
            if not visited[j]:
                visited[j] = 1
            for h in dice:
                if not visited[h]:
                    print(i, j, h)
                    visited[h] = 1

