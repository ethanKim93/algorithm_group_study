A = list(map(int, input().split()))
limit = len(A)
visited=[0]*(limit+1)

def backtrack(arr,i,hap):
    if i > limit-1:
        return
    if hap > 10:
        return
    if hap == 10:
        for j in range(limit):
            if arr[j]:
                print(A[j],end=' ')
        print()
        return
    arr[i] = 1
    backtrack(arr,i+1,hap+A[i])
    arr[i] = 0
    backtrack(arr,i+1,hap)


backtrack(visited,0,0)