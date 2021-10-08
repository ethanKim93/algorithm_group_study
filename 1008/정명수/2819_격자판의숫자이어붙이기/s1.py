import sys
sys.stdin = open('input.txt')

def makenum(a,b,num):
    global numbers
    if len(num) == 7:
        numbers.add(num)
        return
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        di = dx[i]+a
        dj = dy[i]+b
        if 0<=di<4 and 0<=dj<4:
            makenum(di, dj, num+arr[di][dj])

T = int(input())
for tc in range(1,T+1):
    arr = [list(input().split()) for _ in range(4)]
    numbers = set()
    for i in range(4):
        for j in range(4):
            makenum(i,j,arr[i][j])
    print('#{} {}'.format(tc,len(numbers)))
