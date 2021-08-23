import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bus_stations = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for station in range(A, B + 1):
           bus_stations[station] += 1
    P = int(input())
    result = []
    for _ in range(P):
        result.append(bus_stations[int(input())])
    result = " ".join(map(str, result))
    print("#{} {}".format(tc, result))

