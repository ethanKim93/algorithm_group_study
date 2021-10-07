import sys
sys.stdin = open('input.txt')
#곱하면 곱할수록 작아지므로 이를 활용
def percentage(emp,total):
    global maxv
    if total <= maxv:
        return

    if emp==N:
        if total > maxv:
            maxv = total
        return

    for j in range(N):
        if mission[j]: continue
        mission[j]=1
        percentage(emp+1,total*arr[emp][j])
        mission[j]=0
def f(x):
    return float(x)/100

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 함수로 작성하기
    #arr=[list(map(f,input().split())) for _ in range(N)]

    # 람다로 작성하기
    arr = [list(map(lambda x: float(x)/100, input().split())) for _ in range(N)]
    total=100.0
    maxv=-1

    employee = []
    for i in range(1,N+1):
        employee.append(i)

    mission = [0] * (N + 1)

    percentage(0, total)
    print('#{} {:06.6f}'.format(tc, maxv))