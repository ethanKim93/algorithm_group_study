import sys
sys.stdin = open("sample_input.txt")

# 이진탐색과 탐색 횟수를 반홚하는 함수
def binary_search(a_init, a_end, target):
    if target > a_end:
        return 1001
    cnt = 1
    while a_init <= a_end:
        a_center = int((a_init + a_end)/2)
        if target == a_center:
            break
        elif target < a_center:
            a_end = a_center
        else :
            a_init = a_center
        cnt += 1
    return cnt

T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    init = 1
    Astatus = binary_search(init, P, A)
    Bstatus = binary_search(init, P, B)
    result = "0" if Astatus == Bstatus else "B" if Astatus > Bstatus else "A"
    print("#{} {}".format(tc, result))