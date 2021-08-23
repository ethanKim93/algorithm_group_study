arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N  # 썼나 안썼냐 구분해주는 리스트  # [0, 0, 0]


def powerset(idx):  #썼는지 안썼는지 확인할 수 있는 powerset 함수
    lst = []
    if idx == N:
        for index, i in enumerate(sel):
            if i:
                # print(arr[index], end=' ')
                lst.append(arr[index])
        if sum(lst) == 10:
            print(lst)
        return

    sel[idx] = 1  # 사용했다.  # [1, 0, 0]   [1, 1, 0]  [1, 1, 1]   [1, 0, 1]
    powerset(idx+1)     # powerset(1)  powerset(2) powerset(3)  powerset(3)
    sel[idx] = 0  # 뒤에서부터 다시 사용 안한다고 바꿈  # [1, 1, 0]   [1, 0, 0]  [1, 0, 0]
    powerset(idx+1)     # powerset(3)   powerset(2) powerset(3)
powerset(0)
