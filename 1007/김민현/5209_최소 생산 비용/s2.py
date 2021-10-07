import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def BT(no, summary):
    global result

    if summary > result:
        return

    if len(visited) == len(factory):
        if summary < result:
            result = summary
        return

    for idx in range(len(factory)):
        if idx not in visited:
            visited.append(idx)
            summary += factory[no][idx]
            BT(no + 1, summary)
            visited.pop()
            summary -= factory[no][idx]

for tc in range(1, 1 + T):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    result = 100000 #임의의 큰 수
    BT(0, 0) #(공장번호,합계)
    print("#{} {}".format(tc, result))