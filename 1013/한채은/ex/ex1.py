# 주호님 코드
# 공부하려고..

st = "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 "
N = 8
field = [[] for _ in range(N)]
line = list(map(int, st.split()))
check = [True] * N
for i in range(N):
    field[line[2 * i]].append(line[2 * i + 1])
    field[line[2 * i + 1]].append(line[2 * i])

stack = [1]
while stack:
    p = stack.pop()
    if check[p]:
        check[p] = False
        for place in field[p]:
            stack.append(place)
        print(p, end=" ")