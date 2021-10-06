# 연습문제 2 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
# backtracking으로 풀어보기 :(
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

N = 10
for i in range(1 << N):
    total = 0
    sub = []
    for j in range(N):
        if i & (1 << j):
            sub.append(arr[j])
            total += arr[j]

    if total == 10:
        print(sub)

