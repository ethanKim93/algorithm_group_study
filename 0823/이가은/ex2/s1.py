
arr = [i for i in range(1,11)]
N = len(arr)
sel = [0] * N

def powerset(idx, K):
    if len(sel) < N :
        sel[idx] = 1
        powerset(idx+1, K)
        sel[idx] = 0
        powerset(idx+1, K)
    else:
        power_sum = 0
        for i in range(len(arr)):
            if sel[i]:
                power_sum += arr[i]
        if power_sum == K:
            for i in range(len(arr)):
                if i == 1:
                    print(arr[sel.index(i)], end=' ')
                # 모르겠어요..ㅠㅠㅠㅠㅠ
            print()

powerset(0, 10)







'''

arr = [2,4,6]
N = len(arr)
sel = [0] * N

def powerset(idx):
    if idx == N:
        for index, i in enumerate(sel):
            if i:
                print(arr[index], end=' ')
        print()
        return

    sel[idx] = 1
    powerset(idx+1)

    sel[idx] = 0
    powerset(idx+1)

powerset(0)








''''''
'''
