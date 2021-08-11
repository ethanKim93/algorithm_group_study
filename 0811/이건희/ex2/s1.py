import sys
sys.stdin = open("input.txt")

def check(num_list):
    subsets = []
    for i in range(1 << 10):
        temps = []
        for x in range(10):
            if i & (1 << x):
                temps.append(num_list[x])
        subsets.append(temps)

    for i in subsets:
        sm = 0
        for x in i:
            sm += x
        if sm == 0:
            return 1
        return 0

t = int(input())
for tc in range(1, t+1):
    num_list = list(map(int,input().split()))

    print("#{} {}".format(tc, check(num_list)))