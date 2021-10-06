import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)
    ans = 0
    for truck in trucks:
        for i in range(len(w)):
            if truck >= w[i]:
                ans += w[i]
                w.pop(i)
                break
    print('#{} {}'.format(tc, ans))
