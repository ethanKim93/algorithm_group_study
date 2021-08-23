# def powerset(i, N):
#     if i == N:
#         print(arr)
#     else:
#         for j in range(i, N):
#             arr[i], arr[j] = arr[j], arr[i]
#             powerset(i+1, N)
#             arr[i], arr[j] = arr[j], arr[i]
#
# arr = [1,2,3]
# powerset(0, len(arr))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N          # [0, 0, 0]

def Ps(idx, subsum):
    if idx == N:
        if subsum == 10:
            for idx, i in enumerate(sel):
                if i:
                    print(arr[idx], end=' ')
            print()
        return

    else:
        sel[idx] = 1                       #1 [1, 0, 0]       #2 [1, 1, 0]       #3 [1, 1, 1]   #6 [1, 0, 1]
        Ps(idx+1, subsum+arr[idx])         # Ps(1)           #Ps(2)            #Ps(3)         #Ps(3)
        sel[idx] = 0              #4 [1, 1, 0]       #5 [1, 0, 0]       #7 [1, 0, 0]
        Ps(idx+1, subsum)         # Ps(3)           # Ps(2)           # Ps(3)

Ps(0, 0)

