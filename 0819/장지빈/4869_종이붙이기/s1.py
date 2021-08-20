import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    row = int(int(input())/10)
    li = [0, 1, 3]

    for i in range(3, row+1):
        li.append(li[i-1] + (li[i-2]*2))

    ans = li[row]

    print('#{} {}'.format(tc, ans))