import sys
sys.stdin = open('input.txt')
# 계산 효율 최악인 것 같아 자괴감이 드는 코드
T = 10

for tc in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort()
    for i in range(dump):
        boxes[0] += 1
        boxes[-1] -= 1
        boxes.sort()
    print('#{} {}'.format(tc, boxes[-1]-boxes[0]))