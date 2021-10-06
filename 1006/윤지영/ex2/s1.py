li = [1,2,3,4,5,6,7,8,9,10]
visited = [0] * (len(li)+1)
result = []
c = [0] * 2     # 들어가냐 안들어가냐 2가지 경우만 체크

def backtrack(k, input):
    if k == input:
        ans = []
        for i in range(1, k + 1):
            if visited[i] == True:
                if sum(ans) > 10:
                    return
                else:
                    ans.append(li[i - 1])
        if sum(ans) == 10:
            result.append(ans)
    else:
        k += 1
        make_candidates(c)
        for i in range(2):
            visited[k] = c[i]
            backtrack(k, input)

def make_candidates(c):
    c[0] = True
    c[1] = False


backtrack(0,len(li))
print(result)