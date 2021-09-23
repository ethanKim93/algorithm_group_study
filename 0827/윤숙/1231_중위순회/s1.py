import sys
sys.stdin = open('input.txt','r')

def in_order(n):
    if n:
        in_order(int(left[n]))
        print(status[n], end="")
        in_order(int(right[n]))


T = 10
for tc in range(1, T + 1):
    V = int(input())
    left = [0]*(V+1)
    right = [0]*(V+1)
    status = [0] *(V+1)

    for _ in range(V):
        tmp = list(map(str, input().split()))
        status[int(tmp[0])] = tmp[1]
        # print(tmp)
        if len(tmp)==4:
            left[int(tmp[0])]=tmp[2]
            right[int(tmp[0])]=tmp[3]
        if len(tmp)==3:
            left[int(tmp[0])]=tmp[2]

  
    print('#{}'.format(tc), end=" ")
    in_order(1)
    print()

