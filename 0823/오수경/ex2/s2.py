# 합이 10인 부분집합 구하기

arr = range(1, 11)
N = len(arr)
sel = [0] * N   # [0, 0, 0]

def powerset(idx):
    if idx == N:    #idx가 N을 넘어가면 안되니까
        total_lst = []
        for index, i in enumerate(sel):   # i = 1 or 0
            if i:  # i = 1
                total_lst.append(arr[index])
        if sum(total_lst) == 10:
            print(total_lst)
        return
    sel[idx] = 1        # [1, 0, 0]     [1, 1, 0]       [1, 1, 1]       [1, 0, 1]
    powerset(idx+1)     # powerset(1)   powerset(2)     powerset(3)     powerset(3)
    sel[idx] = 0        #-> [1, 1, 0]   [1, 0, 0]       [1, 0, 0]
    powerset(idx+1)     # powerset(3)   powerset(2)     powerset(3)

powerset(0)