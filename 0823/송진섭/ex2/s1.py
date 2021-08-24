# 부분집합 전체 구하기 비트연산자 활용

arr = [1, 2, 3]

for i in range(1 << 3):
    for j in range(len(arr)):
        if i & (1 << j):
            print(arr[j], end=' ')
    print()