import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for i in range(T):
    N = int(input())
    ai = list(input())
    aiList = [0]*10

    for a in range(N):
        aiList[int(ai[a])] += 1

    maxcard = 0
    biggestOne = 0
    for n in range(len(aiList)):
        if int(aiList[n]) >= maxcard:
            maxcard = int(aiList[n])

    for x in range(9, 0, -1):
        if int(aiList[x]) == maxcard:
            biggestOne = x
            break

    print('#{} {} {}'.format(i+1, biggestOne, maxcard))
