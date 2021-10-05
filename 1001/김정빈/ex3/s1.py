"""
부분집합 합 문제 구하기
아래의 10개의 정수 집합에 대한 모든 부분 집합 중 원소의 합이 0이 되는 부분집합을 모두 출력하시오
"""
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)
cnt = 0
for i in range(0, 1<<n):
    res = []
    for j in range(0, n):
        if i & (1 << j):
            res.append(arr[j])
    if sum(res) == 0 and len(res) != 0:
        cnt += 1
        print(res)
print('총 {}개의 부분집합이 존재함'.format(cnt))