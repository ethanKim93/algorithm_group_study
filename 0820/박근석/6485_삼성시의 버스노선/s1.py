import sys
sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    list_a = []
    for i in range(N):
        V = list(map(int, input().split()))
        list_a.append(V)
    print(list_a)
    list_b = [0]*int(input())

    for i in range(len(list_b)):
        list_b[i] = int(input())

    list_c = [0]*len(list_b)
    for i in list_a:
        for j in range(i[0], i[1]+1):
            for k in range(len(list_b)):
                if j == k+1:
                    list_c[k] += 1

    print('#{} {}'.format(tc, ' '.join(map(str, list_c))))
