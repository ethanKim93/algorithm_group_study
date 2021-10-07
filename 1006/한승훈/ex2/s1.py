arr = range(1, 11)
N = len(arr)
sel = [0] * N

def powerset(idx):
    if idx == N:
        total = 0
        stack = []
        for index, i in enumerate(sel):
            if i:
                total += arr[index]
                stack.append(arr[index])
        if total == 10:
            print(*stack)
        return
    sel[idx] = 1
    powerset(idx+1)
    sel[idx] = 0
    powerset(idx+1)

powerset(0)