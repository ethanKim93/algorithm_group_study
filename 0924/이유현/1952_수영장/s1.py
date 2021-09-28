import sys
sys.stdin = open('sample_input.txt')


def pay(m, est):
    global minV

    if m > 12:
        if minV > est:
            minV = est
            return
    else:
        # 1일권
        pay(m+1, est+plan[m]*day)
        # 1달권
        pay(m+1, est+mth)
        # 3달권
        pay(m+3, est+thr_mth)


T = int(input())
for tc in range(1, T+1):
    day, mth, thr_mth, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))

    minV = year
    pay(1, 0)
    print('#{} {}'.format(tc, minV))
