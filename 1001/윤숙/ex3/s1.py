arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

def combination(n, R):
    if R == 0:
        cac=0
        for j in range(len(arr_reault)):
            cac+=arr_reault[j]
        if arr_reault and cac==0:
            print(arr_reault)
    elif n < R:
        return
    else:
        arr_reault[R-1]=arr[n-1]
        combination(n-1,R-1)
        combination(n-1,R)


n=len(arr)
for i in range(n):
    total=[]
    R=i
    arr_reault = [0] * R
    combination(n, R)
