#미완

import sys
sys.stdin = open('sample_input.txt')

T = int(input())


def succese(person,percent):
    global result
    a = result
    if percent > result:
        return

    if len(visited) == len(Pi):
        if percent > result:
            result = percent
        return

    for idx in range(len(Pi)):
        if idx not in visited:
            if not Pi[person][idx]:
                continue
            visited.append(idx)
            percent *= Pi[person][idx]
            succese(person + 1, percent)
            visited.pop()
            percent /= Pi[person][idx]


for tc in range(1,T+1):
    N = int(input())
    Pi = [list(map(int,input().split())) for _  in range(N)]
    visited = []
    result = 1.0


    succese(0, 1)

    print('#{} {}'.format(tc,result))