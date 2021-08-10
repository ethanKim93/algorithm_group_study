import sys
sys.stdin = open('input.txt')



for tc in range(10):
    dumpN = int(input())
    blocks = list(map(int, input().split()))

    while dumpN >= 0:

        dumpN -= 1

        for i in range(len(blocks)):
            for j in range(len(blocks)-1, 0, -1):
                if blocks[j] <= blocks[j-1]:
                    blocks[j], blocks[j-1] = blocks[j-1], blocks[j]
# blocks 버블 정렬

        blocks[0] += 1
        blocks[len(blocks)-1] -= 1

# 버블정렬한 list의 처음 값에 +1, 마지막값에 -1을 하고 다시 버블정렬 반복

    result = blocks[len(blocks) - 1] - blocks[0] + 2
# 2를 안 더해주면 결과값에 2가 빠진 결과가 반환되는데 아마 +, - 하는 과정을 한 번 빼먹는 것 같습니다.
# dumpN 의 조건을 바꿔주게 되면 아예 다른값으로 결과가 나오는데 어떻게 수정해야 할 지 몰라 그냥 2를 더해줬습니다.
    print('#{} {}'.format(tc+1, result))