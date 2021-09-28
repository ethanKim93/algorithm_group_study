import sys
sys.stdin = open('sample_input.txt')

def calc(cost, t):
    global min_cost
    if t > 12:
        if cost < min_cost:
            min_cost = cost
        return
    # 1일권
    calc(cost+d*plan[t], t+1)
    # 1달권
    calc(cost+m1, t+1)
    # 3달권
    calc(cost+m3, t+3)


for tc in range(1, int(input())+1):
    d, m1, m3, yr = map(int, input().split())
    plan = [0]+list(map(int, input().split()))
    min_cost = yr
    calc(0,1)
    print('#{} {}'.format(tc, min_cost))