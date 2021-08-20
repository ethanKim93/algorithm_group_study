import sys
sys.stdin = open('sample_input.txt')

def paper(n):
    p = [1, 3]

    for i in range(2, n):
        p.append(p[i-2] * 2 + p[i-1])
    return p[n-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())//10
    print('#{} {}'.format(tc, paper(N)))