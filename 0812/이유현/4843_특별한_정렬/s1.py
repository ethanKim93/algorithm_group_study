import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    sort_list = []
    while arr:
        maxV = minV = arr[0]
        for num in arr:
            if maxV <= num:
                maxV = num
            if minV >= num:
                minV = num
        arr.remove(maxV)
        arr.remove(minV)
        sort_list.append(maxV)
        sort_list.append(minV)

    print('#{}'.format(tc), end=' ')
    for n in sort_list:
        print(n, end=' ')
    print()




