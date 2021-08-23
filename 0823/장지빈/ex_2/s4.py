arr = range(1, 11)
N = len(arr)
sel = [0] * N

def powerset(idx, subset):
    if idx == N:        #위에 있어야 3번 인덱스에 더이상 접근하지 않는다
        sumls = 0
        ls = []
        for index, i in enumerate(sel):
            if i:
                sumls += arr[index]
                ls.append(arr[index])
        if sumls == subset:
            print(*ls)
        return
    sel[idx] = 1        # 사용 여부에 들어온 idx 사용 체크
    powerset(idx+1, subset)
    sel[idx] = 0
    powerset(idx+1, subset)
powerset(0, 10)     #0 번 인덱스부터 시작