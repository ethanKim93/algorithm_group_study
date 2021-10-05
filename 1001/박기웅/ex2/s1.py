# 6자리 숫자에 대해서 완전 검색을 적용해서 Baby-gin을 검사해보시오

input_str = [
    '124783',
    '667767',
    '054060',
    '101123',
]

def check(p):
    i = cnt = 0
    while i<6:
        if p[i] + 1 == p[i+1] and p[i+1] +1 == p[i+2]:
            cnt += 1
        if p[i] == p[i+1] and p[i+1] == p[i+2]:
            cnt += 1
        i += 3
    return 1 if cnt == 2 else 0

def perm(n,k):
    global ans
    if n == k:
        if check(p):
            ans = 1
    else:
        for i in range(n):
            if not u[i]:
                u[i] = 1
                p[k] = arr[i]
                perm(n, k+1)
                u[i] = 0
            
for strs in input_str:
    print(strs, 'is Baby GIN?')
    ans = 0
    arr = list(map(int, strs))
    p, u = [0]*6, [0]*6
    perm(6, 0)
    print('YES' if ans else 'NO')
