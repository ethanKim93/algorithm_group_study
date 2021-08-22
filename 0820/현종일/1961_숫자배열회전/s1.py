import sys
sys.stdin = open('input.txt')

T = int(input())

def rotate(array):
    s = len(array)
    res = list([0]*s for x in range(s))
    for i in range(s):
        for j in range(s):
            res[j][s-1-i] = array[i][j]
    return res

for tc in range(1, T+1):
    N = int(input())
    array = []
    for i in range(N):
        array.append(list(map(int,input().split())))
    ans = []
    ans.append(rotate(array))
    ans.append(rotate(ans[0]))
    ans.append(rotate(ans[1]))
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(3):
            print(''.join(map(str,ans[j][i])),end= ' ')
        print()