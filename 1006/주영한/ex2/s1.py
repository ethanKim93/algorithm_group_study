a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def backtracking(arr, temp_arr, cnt, total, pos):
    if cnt == total:
        print(*temp_arr)
        return
    
    if cnt > total or pos == len(arr):
        return
    
    temp_arr.append(a[pos])
    backtracking(arr, temp_arr, cnt + a[pos], total, pos + 1)
    temp_arr.pop()
    backtracking(arr, temp_arr, cnt, total, pos + 1)
    return

backtracking(a, [], 0, 10, 0)