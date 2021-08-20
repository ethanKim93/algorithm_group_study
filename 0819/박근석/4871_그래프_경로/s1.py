import sys
sys.stdin = open('sample_input.txt')

def check(t_list, start, end):
    for i in t_list:
        if i[0] == start:
            for k in range(E):
                for j in range(E):
                    if t_list[j][0] == i[1] and t_list[j][1] == end:
                        return 1
                    elif t_list[j][0] == i[1]:
                        start = t_list[j][0]
    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, list(input().split())))

    node_list = [0]*E
    for i in range(E):
        node_list[i] = list(map(int, list(input().split())))

    start, end = list(map(int, list(input().split())))

    print('#{} {}'.format(tc, check(node_list, start, end)))
