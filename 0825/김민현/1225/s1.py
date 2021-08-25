import sys
sys.stdin = open("input.txt")

def trans(data):
    #전체 와일문(data에 0보다 작은 값이 생기면 탈출)
    i = 0
    num = data[0]
    while num>0:
        #1~5까지의 반복문
        i = i%5+1
        #맨앞의 숫자 pop후 -i
        num = data.pop(0)-i
        #맨뒤에 추가
        if num < 0:
            num = 0
        data.append(num)
        a = 1


for _ in range(1, 11):
    tc = int(input())
    data = list(map(int,input().split()))
    trans(data)
    print('#{}'.format(tc),end=' ')
    print(*data)