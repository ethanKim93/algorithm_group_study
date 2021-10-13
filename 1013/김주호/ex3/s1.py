import sys
sys.stdin = open("input.txt")

N = 6
field = [list(map(int, input().split())) for _ in range(6)]
val = field[0][:]
check = [False] * N
check[0] = True

for now in range(N):
    if check[now]:
        for target in range(now + 1, N):
            if not check[target]:
                val[target] = min(field[now][target] + val[now], val[target])
                if val[target] < 10000:
                    check[target] = True

print(val)
