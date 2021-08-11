import sys

sys.stdin = open('input.txt')
T = int(input())

for a in range(1, T + 1):
    arr = list(map(int, input().split()))
    n = len(arr)
    for i in range(1, 1 << n):  # 공집합을 제외하기 위해서 0이 아닌 1부터 시작한다. 0 0이 걸릴 수 있으므로.
        part = 0
        for j in range(n):
            if i & (1 << j):  # i의 j번째 비트가 1인지 아닌지를 리턴한다.
                part += arr[j]
        if not part:  # part가 True가 아니면
            print('#{} 1'.format(a))
            break
    else:
        print('#{} 0'.format(a))
