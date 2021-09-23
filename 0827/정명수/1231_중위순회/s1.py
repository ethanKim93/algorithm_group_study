import sys
sys.stdin = open('input.txt')

def in_order(v):
    global answer
    if v:
        in_order(left[v])
        answer.append(v)
        in_order(right[v])
for tc in range(1,11):
    N = int(input())
    mean = [0]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)
    answer = []
    for _ in range(N):
        li = list(input().split())
        mean[int(li[0])] = li[1]
        if len(li) >= 3:
            left[int(li[0])] = int(li[2])
            if len(li) == 4:
                right[int(li[0])] = int(li[3])
    in_order(1)
    print('#{} '.format(tc),end='')
    for j in answer:
        print(mean[j],end='')
    print()




