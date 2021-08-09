import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())
    build = list(map(int, input().split()))
    allsum = 0
    # print(L)
    # print(builds)
    # print('#{}'.format(L))
    # print('#{} {}'.format(L, builds))
    for i in range(2, L-2):
        if build[i] - build[i-2] >= 0 and build[i] - build[i-1] >= 0:
            if build[i] - build[i + 2] >= 0 and build[i] - build[i + 1] >= 0:
                if build[i+2] >= build[i+1] and build[i+2] >= build[i-1] and build[i+2] >= build[i-2]:
                    allsum += (build[i]-build[i+2])
                elif build[i+1] >= build[i+2] and build[i+1] >= build[i-1] and build[i+1] >= build[i-2]:
                    allsum += (build[i]-build[i+1])
                elif build[i-2] >= build[i+1] and build[i-2] >= build[i-1] and build[i-2] >= build[i+2]:
                    allsum += (build[i]-build[i-2])
                elif build[i-1] >= build[i+1] and build[i-1] >= build[i+2] and build[i-1] >= build[i-2]:
                    allsum += (build[i]-build[i-1])
    print('#{} {}'.format(tc, allsum))

