import sys
sys.stdin = open("input.txt")

for tc in range(1,11):
    dump = int(input())
    boxs = list(map(int, input().split()))

    def dump_func(boxs):
        minbox = maxbox = boxs[0]
        minidx = maxidx = 0
        for idx, box in enumerate(boxs):
            if box > maxbox:
                maxbox, maxidx = box, idx
            if box < minbox:
                minbox, minidx = box, idx
        boxs[maxidx] -= 1
        boxs[minidx] += 1

        minbox = maxbox = boxs[0] #갱신된 박스로 초기화
        minidx = maxidx = 0
        for idx, box in enumerate(boxs):
            if box > maxbox:
                maxbox, maxidx = box, idx
            if box < minbox:
                minbox, minidx = box, idx
        return maxbox-minbox, boxs # 갱신된 후의 높이 차와 박스를 반환

    while (dump>0):
        height_diff, boxs = dump_func(boxs)
        dump -= 1
        if height_diff <= 1:
            break

    print('#{} {}'.format(tc, height_diff))

