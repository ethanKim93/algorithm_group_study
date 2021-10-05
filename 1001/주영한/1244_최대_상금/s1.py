# import sys
import copy
# sys.stdin = open('input.txt')

T = int(input())

def swap():
    max_price = copy.copy(originPrice)
    for i in range(len(max_price)):
        max_idx = i
        for j in range(i + 1, len(max_price)):
            if max_price[max_idx] < max_price[j]:
                max_idx = j
        max_price[i], max_price[max_idx] = max_price[max_idx], max_price[i]

    max_cnt = 0
    swap_idx = 0
    temp_price = copy.copy(originPrice)
    while temp_price != max_price:
        for i in range(swap_idx, len(temp_price)):
            if max_price[swap_idx] == temp_price[i]:
                temp_price[swap_idx], temp_price[i] = temp_price[i], temp_price[swap_idx]
                max_cnt += 1
                swap_idx += 1
                break

    if not max_cnt and swapTime > 1:
        return "".join(max_price)

    if swapTime >= max_cnt:
        new_swap_time = (swapTime - max_cnt) % 2
        if new_swap_time:
            max_price[len(max_price) - 1], max_price[len(max_price) - 2] = max_price[len(max_price) - 2], max_price[len(max_price) - 1]
        return "".join(max_price)
    else:

        max_cnt = 0
        swap_idx = 0
        max_price = copy.copy(originPrice)
        while max_cnt != swapTime:
            max_idx = swap_idx
            swappable = []
            less_cnt = 0
            for i in range(swap_idx + 1, len(max_price)):
                if max_price[swap_idx] > max_price[i]:
                    less_cnt += 1

            for i in range(swap_idx + 1, len(max_price)):
                if max_price[max_idx] < max_price[i]:
                    swappable.clear()
                    swappable.append(i)
                    max_idx = i
                elif max_price[max_idx] == max_price[i]:
                    swappable.append(i)

            if swap_idx != max_idx:
                if len(swappable) > less_cnt:
                    max_price[swap_idx] , max_price[swappable[len(swappable) - 1 - less_cnt]] = max_price[swappable[len(swappable) - 1 - less_cnt]], max_price[swap_idx]
                    max_cnt += 1
                else:
                    max_price[swap_idx] , max_price[swappable[0]] = max_price[swappable[0]], max_price[swap_idx]
                    max_cnt += 1
            swap_idx += 1
        return "".join(max_price)


for tc in range(1, T + 1):
    originPrice, swapTime = input().split()
    originPrice = list(originPrice)
    swapTime = int(swapTime)
    print("#{} {}".format(tc, swap()))