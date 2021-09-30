import sys
sys.stdin = open("sample_input.txt")


table = {
    '211': (3, '0'),
    '221': (2, '1'),
    '122': (2, '2'),
    '411': (1, '3'),
    '132': (1, '4'),
    '231': (1, '5'),
    '114': (1, '6'),
    '312': (1, '7'),
    '213': (1, '8'),
    '112': (3, '9'),
}


def decode_append(decode_sets, passwords):
    for decode_set in decode_sets:
        if decode_set == passwords:
            return
    decode_sets.append(passwords)
    return


def convert_binary(decode_sets):
    for idx, decode_set in enumerate(decode_sets):
        result = ""
        for hex_num in decode_set:
            if hex_num.isdigit():
                hex_num = int(hex_num)
            else:
                hex_num = ord(hex_num) - ord('A') + 10
            cnt = 0
            temp_result = ""
            while cnt < 4:
                temp_result = str(hex_num % 2) + temp_result
                hex_num = hex_num // 2
                cnt += 1
            result += temp_result
        result = result.rstrip('0')
        decode_sets[idx] = result
    return


def go(decode_set, idx):
    result = ""
    while len(result) < 8:
        nums = [0, 0, 0]
        cmp_str = decode_set[idx]
        if cmp_str != '1':
            return (False, None, None)
        cnt = 2
        while True:
            if cmp_str != decode_set[idx]:
                cnt -= 1
                if cnt < 0:
                    break
                nums[cnt] += 1
                cmp_str = decode_set[idx]
            else:
                nums[cnt] += 1
            idx -= 1
        min_num = min(nums)
        for i in range(3):
            nums[i] = nums[i] // min_num
        temp_ratio = "".join(map(str, nums))
        if table.get(temp_ratio):
            zero_nums, converted = table[temp_ratio]
            for j in range(zero_nums * min_num):
                if decode_set[idx] != '0':
                    return (False, None, None)
                idx -= 1
            result = str(converted) + result
        else:
            return (False, None, None)
    return (True, result, len(result) * 7 * min_num)

def code_sum(temp_result):
    odd_set = int(temp_result[0]) + int(temp_result[2]) + int(temp_result[4]) + int(temp_result[6])
    even_set = int(temp_result[1]) + int(temp_result[3]) + int(temp_result[5])
    classification = int(temp_result[7])
    if (odd_set * 3 + even_set + classification) % 10 == 0:
        return (temp_result, odd_set + even_set + classification)
    return (None, 0)

def solve(decode_set):
    results = []
    idx = len(decode_set) - 1
    while idx >= 0:
        flag, temp_result, offset = go(decode_set, idx)
        if flag:
            idx -= offset
            temp_string, num = code_sum(temp_result)
            results.append((temp_string, num))
        else:
            idx -= 1
    return results

T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())
    decode_sets = []
    for row in range(R):
        passwords = input().rstrip('0')
        if passwords:
            decode_append(decode_sets, passwords)
    convert_binary(decode_sets)
    result = 0
    results = []
    for decode_set in decode_sets:
        temp_results = solve(decode_set)
        for temp_result in temp_results:
            if temp_result[0] not in results:
                results.append(temp_result[0])
                result += temp_result[1]
    print("#{} {}".format(tc, result))