arr = range(1, 11)
N = len(arr)
sel = [0] * N  # [0, 0, 0]


def powerset(idx, subsum):
    if idx == N:
        total = 0
        result = []
        for i in range(len(sel)):
            if sel[i]:
                total += arr[i]
                result.append(arr[i])
                if total > subsum:
                    return
        if total == subsum:
            print(*result)
        return
    sel[idx] = 1        # 사용했는지 여부를 확인하면서 idx를 증가 > 최대 idx까지 도착했을때 return
    powerset(idx+1,10)
    sel[idx] = 0        #
    powerset(idx+1,10)
powerset(0,10)
