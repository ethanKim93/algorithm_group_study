import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    arr = [[0] * 100 for _ in range(100)]
    for i in range(100):
        input_arr = list(map(int,input().split()))
        for j in range(100):
            arr[i][j] = input_arr[j]
    results = []

    d1 = 0 # 대각
    d2 = 0 # 역대각
    for k in range(len(arr)):
        x = 0
        y = 0
        d2 += arr[k][99 - k]
        for l in range(len(arr)):
            if k == l:
                d1 += arr[k][l]
            x += arr[k][l]
            y += arr[l][k]

        results.append(d2)
        results.append(d1)
        results.append(y)
        results.append(x)

    max_one = results[0]
    for result in results:
        if result > max_one:
            max_one = result

    print('#{} {}'.format(tc,max_one))