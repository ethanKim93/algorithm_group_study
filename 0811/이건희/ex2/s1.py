import sys
sys.stdin = open("input.txt")

def check(num_list):
    subsets = []

    # Bit mask > make subsets
    for i in range(1 << 10):
        temps = []
        for x in range(10):
            if i & (1 << x):
                temps.append(num_list[x])
        subsets.append(temps)

    for i in subsets:
        if i == []: # 빈리스트 예외처리
            continue

        else:
            sm = 0
            for x in i: # =sum(i)
                sm += x

            if sm == 0:
                return 1

    return 0

t = int(input())
for tc in range(1, t+1):
    num_list = list(map(int,input().split()))

    # Print
    print("#{} {}".format(tc, check(num_list)))