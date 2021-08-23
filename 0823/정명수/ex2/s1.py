arr = range(1,11)
N = len(arr)
sel = [0] * N        #[0, 0, 0]

def powerset(idx):
    if idx ==N:
        total = 0
        j = []
        for index, i in enumerate(sel):
            if i:
                total += arr[index]
                j.append(arr[index])
        if total == 10:
            print(j)
        return
    sel[idx] = 1          #[1, 0, 0]         # [1, 1, 0]     # [1, 1, 1]
    powerset(idx+1)       #powerset(1)       # powerset(2)   # powerset(3)
    sel[idx] = 0          #[0, 0, 0]
    powerset(idx+1)       #powerset(1)
powerset(0)