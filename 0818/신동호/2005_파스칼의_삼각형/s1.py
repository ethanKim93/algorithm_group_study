import sys
sys.stdin = open('input.txt')
# memoization 사용안했을 때
def pascal(ord):
    if ord == 1:
        return [1]
    elif ord == 2:
        return [1, 1]
    row = [1]
    for i in range(ord-2):
        row.append(pascal(ord-1)[i]+pascal(ord-1)[i+1])
    row.append(1)
    return row

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    for i in range(1, N+1):
        for j in range(i):
            print(pascal(i)[j], end=' ')
        print()
