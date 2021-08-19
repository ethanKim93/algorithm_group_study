import sys

sys.stdin = open('input.txt')
T = int(input())


def DPpaper(n):
    if n == 10:
        return 1    # [] #1가지
    elif n == 20:
        return 3  #[----] [   ] [][] (10 과동일 같은 상황) :  총 3가지
    return DPpaper(n - 10) + (2 * DPpaper(n - 20)) #점화식에서 [][] 10과 동일로 치므로 식에서는 총 20일때 2가지가 된다.


for tc in range(1, T + 1):
    n = int(input())
    result=DPpaper(n)
    print('#{} {}'.format(tc,result ))