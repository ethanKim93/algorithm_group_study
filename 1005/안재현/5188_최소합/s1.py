import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    i = 0
    j = 0
    result = arr[i][j]
    while i != N - 1 or j != N - 1:
        if i == N - 1:
            result += arr[i][j + 1]
            j += 1
            # print('#1')
        elif j == N - 1:
            result += arr[i + 1][j]
            i += 1
            # print('#2')
        elif arr[i][j + 1] == arr[i + 1][j] and i + 1 == j + 1 == N - 1:
            result += arr[i][j + 1]
            j += 1
            # print('#5')
        elif arr[i][j + 1] == arr[i + 1][j] and i + 1 == N - 1:
            if arr[i + 1][j + 1] < arr[i + 1][j + 2]:
                result += arr[i + 1][j]
                i += 1
                # print('#6-1')
            elif arr[i + 1][j + 2] < arr[i + 1][j + 1]:
                result += arr[i][j + 1]
                j += 1
            #     print('#6-2')
            # print('#6')
        elif arr[i][j + 1] == arr[i + 1][j] and j + 1 == N - 1:
            if arr[i + 2][j + 1] < arr[i + 1][j + 1]:
                result += arr[i + 1][j]
                i += 1
                # print('#7-1')
            elif arr[i + 1][j + 1] < arr[i + 2][j + 1]:
                result += arr[i][j + 1]
                j += 1
            #     print('#7-2')
            # print('#7')
        elif arr[i + 1][j] < arr[i][j + 1]:
            result += arr[i + 1][j]
            i += 1
            # print('#3')
        elif arr[i][j + 1] < arr[i + 1][j]:
            result += arr[i][j + 1]
            j += 1
            # print('#4')
        elif arr[i][j + 1] == arr[i + 1][j]:
            if arr[i + 2][j + 1] < arr[i + 1][j + 2]:
                result += arr[i + 1][j]
                i += 1
                # print('#8-1')
            elif arr[i + 1][j + 2] < arr[i + 2][j + 1]:
                result += arr[i][j + 1]
                j += 1
                # print('#8-2')
            else:
                result += arr[i][j + 1]
                j += 1
                # print('#8-3')
        #     print('#8')
        # print(i)
        # print(j)
        # print(result)
        # print()

    # print('결과')
    # print(result)
    # print()
    print("#{} {}".format(tc + 1, result))

