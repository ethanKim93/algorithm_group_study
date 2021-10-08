T = int(input())

def bactrackin(pos, temp_result):
    global N, height, result
    if pos == N:
        if temp_result >= height and result > temp_result:
            result = temp_result
        return

    if result < temp_result:
        return

    bactrackin(pos + 1, temp_result + height_set[pos])
    bactrackin(pos + 1, temp_result)    
    return 

for tc in range(1, T + 1):
    N, height = map(int, input().split())
    height_set = list(map(int, input().split()))

    result = 10000 * 21
    bactrackin(0, 0)
    print("#{} {}".format(tc, result - height))