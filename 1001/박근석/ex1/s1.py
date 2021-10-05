a = [3, 5, 1, 6, 7, 2, 8]


def selectionSort(a):
    if a != []:
        x= min(a)
        a.remove(x)
        return [x]+selectionSort(a)
    else:
        return []

# print(selectionSort(a))


def select(b):
    if b == len(a):
        return
    else:
        min1 = a[b]

        for i in range(b+1, len(a)):
            c = min(a[1:])


            if a[i] < min1:
                a[b], a[i] = a[i], a[b]
        select(b+1)

print(select(0))


# print(a.index(6))
#
# def select(a):
#     if len(a) == 1:
#         return
#     else:
#         x = a
#         min1 = x[0]
#         min2 = min(x[1:])
#         if min2 < min1:
#
#
#     min1 = a[]