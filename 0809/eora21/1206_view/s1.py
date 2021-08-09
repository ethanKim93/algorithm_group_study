import sys
sys.stdin = open("input.txt")

for case in range(10):
    L = int(input())
    buildings = list(map(int, input().split()))
    for i in range(2, len(buildings) - 2):
        pass
    print("#{} {}".format(case + 1))