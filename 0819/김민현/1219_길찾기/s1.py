import sys
sys.stdin = open("input.txt")

for tc in range(1,11):
    tc,case_len = map(int,input().split())
    mat = [[0]*100 for _ in range(100)]
    visit = [0]*100
    str_list = list(map(int,input().split()))
    for i in range(0,len(str_list),2):
        mat[str_list[i]][str_list[i+1]] = 1

    visit[0] = 1
    start = 0
    stack = [0]
    result = 0
    i = 0
    while i < 100:
        k = i
        f =k
        if mat[start][i] == 1 and visit[i] != 1:
            if i == 99:
                result = 1
                break
            else:
                start = i
                visit[i] = 1
                stack.append(i)
                i = 0
        elif i == 99:
            if len(stack) != 0:
                start = stack.pop(-1)
                i = 0
            else:
                result = 0
                break
        else:
            i += 1

    print('#{} {}'.format(tc,result))

