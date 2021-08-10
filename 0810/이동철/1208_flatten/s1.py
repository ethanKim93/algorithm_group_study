import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dump_cnt = int(input())
    dump_heights = list(map(int, input().split()))
    for _ in range(dump_cnt):
        for i in range(len(dump_heights)-1, 0, -1):
            for j in range(0, i):
                if dump_heights[j] > dump_heights[j+1]:
                    dump_heights[j], dump_heights[j+1] = dump_heights[j+1], dump_heights[j]
        max_d = dump_heights[-1]
        min_d = dump_heights[0]
        index_max_d = [n for n, x in enumerate(dump_heights) if x == max_d]
        index_min_d = [n for n, x in enumerate(dump_heights) if x == min_d]

        dump_heights[index_max_d[-1]] -= 1
        dump_heights[index_min_d[0]] += 1

    max_dd = 0
    min_dd = 0
    for k in range(len(dump_heights)):
        for i in range(len(dump_heights)-1, 0, -1):
            for j in range(0, i):
                if dump_heights[j] > dump_heights[j+1]:
                    dump_heights[j], dump_heights[j+1] = dump_heights[j+1], dump_heights[j]
        max_dd = dump_heights[-1]
        min_dd = dump_heights[0]

    print('#{} {}'.format(tc, max_dd-min_dd))
