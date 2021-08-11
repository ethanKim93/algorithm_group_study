import sys
sys.stdin = open('input.txt')

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

for tc in range(1, 11):
    dump_max = int(input())
    box_list = bubbleSort(list(map(int,input().split())))

    dump_cnt = 0
    dump_status = 2

    while dump_cnt < dump_max:
        if(dump_status <= 1):
            break
        else:
            box_list[0], box_list[-1] = box_list[0]+1, box_list[-1]-1
            box_list = bubbleSort(box_list)
            dump_cnt += 1
            dump_status = box_list[-1] - box_list[0]
            
    print('#{} {}'.format(tc, dump_status))

