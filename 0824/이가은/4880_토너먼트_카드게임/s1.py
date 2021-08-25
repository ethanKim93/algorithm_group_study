import sys
sys.stdin = open('sample_input.txt')

# def fight(a, b):
#     if
#
# def tour(li):
#     tour_N = len(li)
#     tour_S =

T = int(input())
for tc in range(T):
    N = int(input())
    li = list(map(int, input().split()))
    li_dic = {key} : {value} for key, value in enumerate(li)
    print(li_dic)

