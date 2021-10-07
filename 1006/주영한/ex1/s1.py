def merge(left, right):
    left_idx = 0
    right_idx = 0
    result = [0] * (len(left) + len(right))

    while left_idx < len(left) or right_idx < len(right):
        if left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                result[left_idx + right_idx] = left[left_idx]
                left_idx += 1
            else:
                result[left_idx + right_idx] = right[right_idx]
                right_idx += 1
        elif left_idx < len(left):
            for l in range(left_idx, len(left)):
                result[l + right_idx] = left[l]
            left_idx = len(left)
        elif right_idx < len(right):
            for r in range(right_idx, len(right)):
                result[left_idx + r] = right[r]
            right_idx = len(right)
    return result

def merge_sort(m_list):
    if len(m_list) == 1:
        return m_list
    
    middle = len(m_list) // 2
    left = merge_sort(m_list[:middle])
    right = merge_sort(m_list[middle:])

    return merge(left, right)


a = [11, 45, 23, 81, 28, 34]
b = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
c = [1, 1, 1, 1, 1, 0, 0, 0, 0]

print(a)
print(merge_sort(a))

print(b)
print(merge_sort(b))

print(c)
print(merge_sort(c))
