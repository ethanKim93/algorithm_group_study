import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    tmp = ''
    result = "OFF"

    while M > 1:
        tmp = (str(M % 2)) + tmp
        M //= 2
    tmp = str(M) + tmp

    if tmp[len(tmp)-N::] == "1" * N:
        result = "ON"
    print("#{} {}".format(tc, result))
