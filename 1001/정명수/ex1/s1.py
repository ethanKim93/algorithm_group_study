a = [88, 12, 46, 48, 32, 65, 48, 1, 989, 23, 4, 89]

def sorting(i):
    if i == len(a)-1:
        print(a)
        return
    if min(a[i:])==a[i]:
        sorting(i+1)
    else:
        j = a[i:].index(min(a[i:]))+i
        a[i],a[j] = a[j],a[i]
        sorting(i+1)
sorting(0)