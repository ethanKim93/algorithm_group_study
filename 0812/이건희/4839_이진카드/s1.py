import sys

sys.stdin = open("input.txt")
t = int(input())

def binary_search(l, r, goal):
    cnt = 0
    while True:
        if l > r: # 못 찾았을 때, 최대 장 수 리턴
            cnt = 1000
            break

        # 찾기
        cnt += 1
        middle = int((l+r)/2)

        if middle == goal:
            return cnt

        elif middle < goal:
            l = middle

        elif middle > goal:
            r = middle

    return cnt

for tc in range(1, t + 1):
    p, pa, pb = map(int, input().split())
    l, r = 1, p # l=start, r=end

    res_pa = binary_search(l, r, pa) # A count
    res_pb = binary_search(l, r, pb) # B count

    if res_pa > res_pb:
        ans = "B"
    elif res_pa < res_pb:
        ans = "A"
    else:
        ans = 0

    print("#{} {}".format(tc, ans))