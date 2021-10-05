def selectionsort(a_list):
    if a_list:
        min_num = min(a_list)
        a_list.remove(min_num)
        return [min_num] + selectionsort(a_list)
    else:
        return []



def selectionsort2(a_list, i, n):
    if i == n:
        return -1
    min_idx = a_list.index(min(a_list))
    if min_idx != i:
        a_list[min_idx], a_list[i] = a_list[i], a[min_idx]
    selectionsort2(a_list, i+1, n)




a = [5, 4, 2, 1, 3]
b = selectionsort(a)
print(b)


