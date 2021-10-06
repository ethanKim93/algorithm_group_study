import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100000000)

def merge(left, right):
    global cnt
    # result = [0]*1000001
    result = [0] * (len(left)+len(right))
    li, ri, i = 0, 0, 0
    if left[-1] > right[-1]:
        cnt += 1
    while li < len(left) or ri < len(right):
        if li < len(left) and ri < len(right):
            if left[li] <= right[ri]:
                result[i] = left[li]
                i += 1
                li += 1
            else:
                result[i] = right[ri]
                i += 1
                ri += 1
        elif li < len(left):
            result[i] = left[li]
            i += 1
            li += 1
        elif ri < len(right):
            result[i] = right[ri]
            i += 1
            ri += 1
    return result
    # result = []
    # while len(Lli) > 0 or len(Rli) > 0:
    #     if len(Lli) > 0 or len(Rli) > 0:
    #         if Lli[-1] > Rli[-1]:
    #             ans.append(Lli[-1])
    #         if Lli[0] <= Rli[0]:
    #             result.append(Lli.pop(0))
    #         else:
    #             result.append(Rli.pop(0))
    #     elif len(Lli):
    #         result.append(Lli.pop(0))
    #     elif len(Rli):
    #         result.append(Rli.pop(0))
    # return result

def merge_sort(li):
    middle = len(li)//2
    if len(li) == 1:
        return li
    left = merge_sort(li[:middle])
    right = merge_sort(li[middle:])
    return merge(left, right)

for tc in range(1, int(input())+1):
    N = int(input())
    li = list(map(int, input().split()))        # 홀수일 경우 오른쪽이 한개 더 작음([0://2])
    ans = []
    cnt = 0
    merged = merge_sort(li)
    print('#{} {} {}'.format(tc, merged[N//2], cnt))