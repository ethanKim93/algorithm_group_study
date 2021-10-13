import sys
sys.stdin = open('sample_input.txt')

# swap으로 해결, 시간 초과
# def cook(ind):
#     global minimum
#     if ind == N//2:
#         A = B = 0

#         for i in range(N//2):
#             for j in range(N//2):
#                 A += mat[used[i]][used[j]]
#                 B += mat[used[i+N//2]][used[j+ N//2]]


#         if minimum > abs(A-B):
#             minimum = abs(A-B)
#         return
#     else:
#         for i in range(ind, N):
#             used[i], used[ind] = used[ind], used[i]
#             cook(ind + 1)
#             used[i], used[ind] = used[ind], used[i]
            
def cook(ind):
    global minimum

    for num in range(1 << N):
        cnt = 0
        for i in range(N):
            if num & (1 << i):
                cnt += 1
        if cnt == N//2:
            A = B = 0
            for i in range(N):
                for j in range(N):
                    if (num & 1 << i) and (num & 1 << j):
                        A += mat[i][j]
                    elif (not (num & 1 << i)) and (not (num & 1 << j)):
                        B += mat[i][j]
            if minimum > abs(A-B):
                # print(A, B, num)
                minimum = abs(A-B)



T = int(input())    

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    used = [i for i in range(N)]
    minimum = 987654321
    cook(0)
    print('#{} {}'.format(tc, minimum)) 
