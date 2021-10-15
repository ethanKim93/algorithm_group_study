# 왜 10개중에 1개가 통과를 안하냐...
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr2 = []
    group = []
    cnt = 0
    for j in range(100):
        group.append([])
    for i in range(0, len(arr), 2):
        arr2.append((arr[i], arr[i + 1]))
    for k in range(len(arr2)):
        group[arr2[k][0]].append(arr2[k][1])
    group2 = []
    for q in range(len(group)):
        if group[q]:
            for a in range(len(group[q])):
                if group[q][a] not in group2:
                    group2.append(group[q][a])
                else:
                    group2.append(q)
    for r in range(N):
        if not group[r] and r not in group2:
            cnt += 1
    group3 = []
    for q in range(len(group)):
        for w in range(len(group[q])):
            if group[group[q][w]]:
                for s in range(len(group[group[q][w]])):
                    group3.append(group[group[q][w]][s])
                group[group[q][w]] = []
    if N - len(group2) != 0:
        print("#{} {}".format(tc + 1, N - len(group2)))
    else:
        print("#{} {}".format(tc + 1, 1))
