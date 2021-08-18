import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    pipe = input()

    start = end = cnt = 0
    for p in range(len(pipe)):
        if pipe[p] == "(":
            start += 1
        elif pipe[p] == ")":
            start -= 1
            if pipe[p-1] == "(":
                cnt += start
            else:
                cnt += 1
    print('#{} {}'.format(tc, cnt))
