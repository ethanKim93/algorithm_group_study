import sys
sys.stdin = open("input.txt")

def get_max_earn(start_idx, prices):
    local_max = 0
    local_max_idx = 0
    for idx in range(start_idx, len(prices)):
        if prices[idx] > local_max:
            local_max = prices[idx]
            local_max_idx = idx
    local_max_idx = local_max_idx + 1
    temp_spent = (local_max_idx - start_idx) * local_max
    for idx in range(start_idx, local_max_idx):
        temp_spent -= prices[idx]
    return temp_spent, local_max_idx


T = int(input())
for tc in range(1, T + 1):
    days = int(input())
    spent = 0
    start_idx = 0
    prices = list(map(int, input().split()))
    while(start_idx < len(prices)):
        temp_spent, temp_idx = get_max_earn(start_idx, prices)
        spent += temp_spent
        start_idx = temp_idx

    print("#{} {}".format(tc, spent))
