import sys
sys.stdin = open('sample_input.txt')

def pair_find(t):
    global pair

    for p in pair:
        pass
    p = 0
    while p <= len(pair):
        if vote[t] in pair[p]:
            pair[p].add(vote[t+1])
        elif vote[t+1] in pair[p]:
            pair[p].add(vote[t])
        else:
            pair.append(set([vote[t], vote[t+1]]))
        p += 1
        break

    return pair

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    vote = list(map(int, input().split()))
    pair = [set([vote[0], vote[1]])]

    for i in range(2, 2*M, 2):
        pair_find(i)

    print('#{} {}'.format(tc, len(pair)))
