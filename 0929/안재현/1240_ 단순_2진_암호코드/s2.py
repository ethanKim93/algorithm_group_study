import sys

sys.stdin = open("input.txt")

amho = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    de = -1
    for i in range(N):
        if "1" in arr[i]:
            de = i
            break
    arr = arr[de:de + 7]
    end_c = M
    for i in range(M - 1, -1, -1):
        if arr[0][i] == "1":
            end_c = i
            break

    Bbit = arr[0][end_c - 55:end_c + 1]

    lst = []
    for i in range(0, 56, 7):
        key = Bbit[i:i + 7]
        lst.append(amho[key])

    a = 0
    for i in range(8):
        if (i + 1) % 2:
            a += int(lst[i]) * 3
        else:
            a += int(lst[i])

    result = 0
    if a % 10 == 0:
        result = sum(lst)

    print("#{} {}".format(tc, result))