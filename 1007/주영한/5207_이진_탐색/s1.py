def check(arr, num):
    start_idx = 0
    end_idx = len(arr) - 1
    middle = (start_idx + end_idx) // 2

    if num > arr[middle]:
        flag = True
        start_idx = middle + 1
    elif num < arr[middle]:
        flag = False
        end_idx = middle - 1
    else:
        return 1

    while start_idx <= end_idx:
        middle = (start_idx + end_idx) // 2
        if num > arr[middle]:
            if flag:
                return 0 
            flag = True
            start_idx = middle + 1
        elif num < arr[middle]:
            if not flag:
                return 0 
            flag = False
            end_idx = middle - 1
        else:
            return 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))
    n_list.sort()
    m_list = list(map(int, input().split()))
    result = 0
    for i in range(M):
        result += check(n_list, m_list[i])
    print("#{} {}".format(tc, result))