import sys
sys.stdin = open("input.txt")

def in_order(v):
    if v:
        in_order(left[v])
        print(chars[v],end='')
        in_order(right[v])

for tc in range(1,11):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N + 1)
    chars = [0] * (N + 1)
    for i in range(N):
       data = list(input().split())
       for j in range(len(data)): #데이터 길이 만큼 반복
            if j == 0:
                node = int(data[j])
            elif j == 1:
                chars[node] = data[j]
            elif j == 2:
                left[node] = int(data[j])
            elif j == 3:
                right[node] = int(data[j])
    print('#{} '.format(tc),end='')
    in_order(1)
    print()