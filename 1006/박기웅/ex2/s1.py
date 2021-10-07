# 비트연산자 이용 완전탐색...
# arr = list(range(1, 11))

# for i in range(1, 1<<10):
#     partial = []
#     for j in range(10):
#         if i & (1<<j):
#             partial.append(arr[j])
#     if sum(partial) == 10:
#         print(partial)



# 어떤 원소가 포함됬는지 아닌지 후보를 만듦
# def make_candidates(arr, k, n, c, ncands):
#     c[0] = 1
#     c[1] = 0
#     ncands = 2

def process_solution(k):
    for i in range(10):
        if visited[i]: print(arr[i], end=' ')
    print()


# def backtrack(k, s):
#     if s>10: return
#     if k == 10 and s == 10: process_solution(k)
#     else:
#         # make_candidates(arr, k+1)
#         for i in range(2):
#             visited[k] = c[i]
#             backtrack(k+1, s+arr[k])

def backtrack(k, s):
    if s>10: return
    if k == 10:
        if s == 10:
            for i in range(10):
                if arr[i]: print(nums[i], end=' ')
            print('sum:',s)
    else:
        for i in range(2):
            arr[k] = c[i]
            backtrack(k+1, s+nums[k]*c[i])
        

nums = list(range(1,11))
arr = [0]*10
# 어떤 원소가 포함됬는지 아닌지 여부
c = [1, 0]
backtrack(0, 0)