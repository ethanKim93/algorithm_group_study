import sys
sys.stdin=open('input.txt')
T=int(input())

def CacSum(arr):
    n = len(arr)
    # (1<<10) 1024번 돌고
    i = 0
    F = 1 << n

    while i <= F:
        i += 1
        # 안에서 10번돌고
        arr_s = []
        for j in range(n):
            # 1 2 4 8 16 32 64 128 512 1024과 & 연산 비교 같을 시에만 출력..
            if i & (1 << j):
                arr_s.append(arr[j])
                ans = 0
                for k in range(len(arr_s)):
                    ans += arr_s[k]
            # print(arr_s)
                if ans == 0:
                    return 1
        if i==F:
            return 0





for tc in range(1,T+1):
    arr=list(map(int,input().split()))
    """
[19, 6, 16, 19, 15, 16, 8, 13, 16, 10]
[-20, -6, -13, 3, -19, -9, 19, -3, 9, 4]
[7, 7, 19, 1, -18, 5, -9, -11, 19, 18]
 
    """
    result=CacSum(arr)
    print('#{} {}'.format(tc,result))







"""
011 011 011  011 
100 011 010  001 
=0   =0  =2   =1     
"""
