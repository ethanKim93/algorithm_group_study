import sys
sys.stdin = open('sample_input.txt')

def cheeze():
    pass

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    pizza_li= list(map(int, input().split()))
    pizza = []
    for i in range(1, len(pizza_li)+1):
       pizza.append([i, pizza_li[i-1]])
    print(pizza_li)
    # print('#{} {}'.format(tc+1,*pizza(N,M)))