import sys
sys.stdin = open("sample_input.txt")

T=int(input())

def check(n):
    if n :
        check(left[n])
        check(right[n])
        visited.append(n)
        
for tc in range(1,T+1):
    E,N = map(int,input().split())
    visited = []
    li = list(map(int,input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    for i in range(E):
        parent = li[i*2]
        child = li[i*2+1] 
        if left[parent] == 0 :
            left[parent] = child
        else:
            right[parent] = child
    check(N)
    cnt = 1
    for res in visited:
        if res == N:
            break
        else:
            cnt += 1
    print(f"#{tc} {cnt}")
    
    

