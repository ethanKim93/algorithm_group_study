arr = list(range(1, 11))
N = len(arr)
sel = [0] * N

def powerset(idx, subsum):
    if subsum > 10:
        return
    elif subsum == 10:
        for index, i in enumerate(sel):
            if i:
                print(arr[index], end=' ')
        print()
        return
    elif idx == N:
        total = 0
        for index, i in enumerate(sel):
            if i:
                total += arr[index]
        if total == 10:
            print(arr[index], end=' ')
        else:
            return
        print()
        return
    sel[idx] = 1
    powerset(idx+1, subsum + arr[idx])
    sel[idx] = 0
    powerset(idx+1, subsum)


powerset(0, 0)


# # 교재에 있는것 그대로 씀
# def construct_candidates(a, k, input, c):
#     c[0] = True
#     c[1] = False
#     return 2
#
#
# def backtrack(a, k, input):
#     global MAXCANDIDATES
#     c = [0] * MAXCANDIDATES
#
#     if k == input:
#         process_solution(a, k)
#     else:
#         k += 1
#         ncandidates = construct_candidates(a, k, input, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k, input)
#
#
# MAXCANDIDATES = 100
# NMAX = 100
# a = [0] * NMAX
# backtrack(a, 0, 3)