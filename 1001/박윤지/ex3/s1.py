# 아래 10개 정수 집합에 대한 모든 부분집합 중 원소들의 합이 0이 되는 부분집합 출력

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

# 바이너리 카운팅으로 부분집합 생성
sublist = []
for i in range(0, 2**len(arr)):  # 0부터 2**n-1 까지 10진수 돌리기
    subset = []
    for j in range(len(arr)-1, -1, -1):
        if i & (1 << j):
            subset.append(arr[j])
    sublist.append(subset)

ans = []
for sub in sublist:
    if sum(sub) == 0:
        ans.append(sub)
print(ans)


###########################################

# # 2. 부분집합(조합) 생성: 재귀호출 이용
# def comb(n, r):  # n개의 원소에서 r개를 선택 (5, 3)
#     if r == 0:
#         print(tr)
#     elif n < r:
#         return
#     else:
#         tr[r-1] = an[n-1]
#         comb(n-1, r-1)
#         comb(n-1, r)  # 마지막 1개 선택하기 전으로 돌아가서 위에서 못넣은 그 전 an 원소 넣기
#
# n = 5
# r = 3
# an = [1, 2, 3, 4, 5]
# tr = [0 for _ in range(r)]
# comb(n, r)
