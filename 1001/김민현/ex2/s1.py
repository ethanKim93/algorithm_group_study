def conNum(arr):
    cnt = 0
    if arr[0] == arr[1]-1 == arr[2]-2:
        cnt += 1
    if arr[3] == arr[4]-1 == arr[5]-2:
        cnt += 1
    return cnt
def triple(arr):
    cnt = 0
    if arr[0] == arr[1] == arr[2]:
        cnt += 1
    if arr[3] == arr[4] == arr[5]:
        cnt += 1
    return cnt

def babygin(arr):

    if conNum(arr) + triple(arr) == 2:
        return True
    else:
        return False


arr = [1,1,1,4,2,3]
print(babygin(arr))