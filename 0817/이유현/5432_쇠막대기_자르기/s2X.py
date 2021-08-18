import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    pipe = input().split('()')

    start = cnt = 0
    for p in pipe:
        if ")" in p:
            cnt += p.count(")")
            start -= p.count(")")

            if start == 0:
                cnt += p.count(")")

            if "(" in p:
                start += p.count("(")
                cnt += start
        else:
            start += p.count("(")
            cnt += start

    print('#{} {}'.format(tc, cnt-len(pipe[-1])))

