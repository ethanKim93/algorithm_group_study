
n, m = map(int,input().split())
dice = [1,2,3,4,5,6]
def dice1(k, cnt):
    global ans
    if cnt == 3:
        print(ans)

    for i in range(6):
        if temps[k] <= 3:
            temps[k] += 1
            ans.append(dice[i])
            dice1(k+1, cnt +1)
            ans.pop()
            temps[k] -= 1
if m == 1:
    temps = [0] * 3
    ans = []
    dice1(0, 0)
#
# def dice2(cnt):
#     if cnt == 3:
#         print(ans)
#     for i in range(3)
#
# if m == 2:
#     temps = [0] * 3
#     ans = []
#     dice2(0)