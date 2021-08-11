import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr) #부분집합의 수를 구하기 위한 원소의 개수

    for i in range(1, 1<<n): #1은 공집합일때를 제외하기 위해서
        part = 0
        for j in range(n+1):
            if i & (1<<j): #1이 있을 때 인덱스 값을 part에 넘겨주는 if
                part += arr[j] #부분집합을 다 더함
        if not part: #part 0이면
            print('#{} 1'.format(tc))
            break
    else:
        print('#{} 0'.format(tc))