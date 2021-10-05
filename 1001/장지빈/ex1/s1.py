li = [3, 4, 1, 2, 56, 7, 78, 8]

def s_sort(ls, N):
    if N == len(li):
        return ls
    else:
        min_n = N
        for i in range(N, len(li)):
            if li[i] < li[min_n]:
                min_n = i
        li[N], li[min_n] = li[min_n], li[N]
        return s_sort(ls, N+1)

print(s_sort(li, 0))
        

