import sys
sys.stdin = open('input.txt')
# 버블 소트로 해결 완료
# 버블 소트 정의
T = 10
def box_sort(boxes):
    for i in range(len(boxes)-2):
        for j in range(len(boxes)-1-i):
            if boxes[j] > boxes[j+1]:
                boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
    return boxes


for tc in range(1, T+1):
    dump = int(input())
    Boxes = list(map(int, input().split()))
    box_sort(Boxes)

    for i in range(dump): # 모든 시행을 일일히 해주고, 시행할 때마다 소팅한다
        Boxes[0] += 1
        Boxes[-1] -= 1
        box_sort(Boxes)
    print('#{} {}'.format(tc, Boxes[-1]-Boxes[0]))