arr = range(1,11)
N = len(arr)

sel = [0] * N #사용여부 확인 # [0,0,0]

def powerset(idx):
    if idx == N:
        total = 0
        for index, i in enumerate(sel):
            if total > 10:
                break
            elif i:
                total += arr[index]
        if total == 10:
            for index, i in enumerate(sel):
                if i:
                    print(arr[index],end =' ')
            print()
        return
                        #N = 3일때 기준,
    sel[idx] = 1        #1#[1,0,0]        2#[1,1,0]        3#[1,1,1]        6#[1,0,1]
    powerset(idx+1)     #powerset(1)    #powerset(1)    #powerset(1)    #powerset(1)
    sel[idx] = 0        #4#[1,1,0]        5#[1,0,0]        7#[1,0,0]
    powerset(idx+1)   #powerset(3)    #powerset(2)    #powerset(3)
powerset(0)
