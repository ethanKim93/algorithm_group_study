import sys
sys.stdin = open('sample_input.txt')

T= int(input())
for test_case in range(1,T+1):
    N = int(input())
    squares = []
    for n in range(N): # 개수만큼 사각형 만들기
        sq = list(map(int, input().split()))
        squares.append(sq)
    arr1 = [[0]*10 for _ in range(10)]
    arr2 = [[0]*10 for _ in range(10)]

    for square in squares:
        for i in range(square[0],square[2]+1):
            for j in range(square[1],square[3]+1):
                if square[4]==1:
                    arr1[i][j] +=1
                else:
                    arr2[i][j] +=1
    counter = 0
    for i in range(10):
        for j in range(10):
            if arr1[i][j]>0 and arr2[i][j]>0:
                counter += 1
    print('#{} {}'.format(test_case,counter))


