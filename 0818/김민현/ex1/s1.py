def push(arr,item):
    arr.append(item)

def pop(arr):
    if len(arr) == 0:
        return
    else:
        arr.pop(-1)

arr = []
push(arr,1)
push(arr,2)
push(arr,3)
pop(arr)
print(arr)

