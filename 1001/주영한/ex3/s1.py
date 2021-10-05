def get_subset(num_list, cnt, sub_set):
    if cnt == len(num_list):
        if sub_set:
            result = 0
            for elem in sub_set:
                result += elem
            if not result:
                print(*sub_set)
        return
    

    get_subset(num_list, cnt + 1, sub_set)

    sub_set.append(num_list[cnt])
    get_subset(num_list, cnt + 1, sub_set)
    sub_set.pop()
    return


num_list = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
get_subset(num_list, 0, [])