arr = [1,1,1,1,1,0,0,0,0,0]

def quick(pivot, start, end):
    i = start
    j = end
    while i < j:
        while arr[i] <= arr[pivot] and i < len(arr) - 1:
            i += 1
        while arr[j] >= arr[pivot] and j > pivot:
            j -= 1
        if i > j:
            arr[pivot], arr[j] = arr[j], arr[pivot]
            quick(pivot, pivot, j-1)
            quick(j+1, j+2, len(arr) - 1)
            break
        if i == j:
            arr[pivot], arr[j] = arr[j], arr[pivot]
            i = start
            j = end
            continue
        arr[i], arr[j] = arr[j], arr[i]

quick(0, 1, len(arr) - 1)
print(arr)