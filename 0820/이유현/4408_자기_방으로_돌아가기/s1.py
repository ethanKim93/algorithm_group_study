import sys
sys.stdin = open('sample_input.txt')


def div(num_str):
    return (int(num_str)+1) // 2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = [list(map(div, input().split())) for _ in range(N)]
    corridor = [0] * 201

    for s in students:
        if s[0] < s[1]:
            for idx in range(s[0], s[1]+1):
                corridor[idx] += 1

        elif s[0] > s[1]:
            for idx in range(s[1], s[0] + 1):
                corridor[idx] += 1
    print('#{}'.format(tc), end=' ')
    max_ans = 0
    for ans in corridor:
        if ans > max_ans:
            max_ans = ans
    print(max_ans)