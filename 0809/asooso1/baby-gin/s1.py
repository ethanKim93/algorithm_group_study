import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    data = list(map(int, list(input())))
    counts = [0] * 10
    for i in range(6):
        counts[data[i]] += 1
    print(counts)
    i = 0
    triplet = 0
    run = 0
    while i < 10:
        if counts[i] >= 3:
            counts[i] -= 3
            triplet += 1
            continue
        if counts[i] and counts[i+1] and counts[i+2]:
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            run += 1
            continue
        i += 1

    if triplet + run == 2:
        print('#{} Baby Gin'.format(tc))
    else :
        print('#{} No Baby Gin'.format(tc))