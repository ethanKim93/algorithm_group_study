arr=[1,2,3,4,5,6,7,8,10]


def backtracking(cnt,k): # cnt 후보선택수, k 선택해야할 후보자 수

    if cnt==k: #선택 명수에 도달
        cac=sum(arr_c)
        if cac==10:
            print(arr_c)
        return

    cnt += 1 #후보 선택시 카운트
    for i in range(size):
        if visited[i]:
            continue
        visited[i]=1
        arr_c[cnt]=arr[i]
        backtracking(cnt,k)
        visited[i]=0



size=len(arr)
arr_c = [0] * (size+1)
visited=[0]*(size+1)
for i in range(size):
    backtracking(0,i)