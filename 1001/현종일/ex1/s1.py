input_list = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]


def sort(input_list, s, e):
    min_idx = s

    if s == e:
        return

    for j in range(s+1, e, 1):
        if input_list[j] < input_list[min_idx]:
            min_idx = j

    input_list[s], input_list[min_idx] = input_list[min_idx], input_list[s]
    sort(input_list, s + 1, e)


sort(input_list, 0, 10)
print(input_list)