A = list(map(int,input().split()))

def partition(arr, l, h):
    pivot = arr[h]

    i = l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1

def quick(arr,l,h):
    if l < h:
        p = partition(arr,l,h)
        quick(arr,l,p-1)
        quick(arr,p+1,h)
    return arr

quick(A,0,len(A)-1)
print(A)