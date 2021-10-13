# 시도 1
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))

    food1 = 0
    food2 = 0
    result = 40001
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                food1 = arr[i][j] + arr[j][i]
                for k in range(len(arr)):
                    for q in range(len(arr)):
                        if k != i and q != j and k != j and q != i and k != q:
                            food2 = arr[k][q] + arr[q][k]
                            print('i{}'.format(i))
                            print('j{}'.format(j))
                            print('k{}'.format(k))
                            print('q{}'.format(q))
                            print(food1)
                            print(food2)
                            print('food12')
                            if result > abs(food1 - food2):
                                result = abs(food1 - food2)
                                print(result)
                                print('resulttmp')
    print(result)
    print('result')
