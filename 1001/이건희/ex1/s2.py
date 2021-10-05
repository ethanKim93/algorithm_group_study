my_list = [5,2,7,1,3,8,9,3,5,2]

def selection_sort_recursion(my_list, s, e):
    min_idx = s
    if s == e:
        return

    for j in range(s+1,e,1):
        if my_list[j] < my_list[min_idx]:
            min_idx = j

    my_list[s], my_list[min_idx] = my_list[min_idx], my_list[s]
    selection_sort_recursion(my_list, s+1, e)

selection_sort_recursion(my_list,0,10)
print(my_list)