import sys
sys.stdin = open("sample_input.txt")

def exchange_num(num_arr, to_exchange):
    result = 0
    for i in range(len(num_arr)):
        result += num_arr[i]*(to_exchange**(len(num_arr)-i-1))
    return result

for tc in range(1, int(input())+1):
    num_2 = list(map(int, input()))
    num_3 = list(map(int, input()))

    result = 0

    for j in range(len(num_2)):
        if result:
            break
        for k in range(2):
            tmp_2 = num_2[j]
            if num_2[j] != k:
                num_2[j] = k
                ex_2 = exchange_num(num_2, 2)
                for l in range(len(num_3)):
                    for m in range(3):
                        tmp_3 = num_3[l]
                        if num_3[l] != m:
                            num_3[l] = m
                            if ex_2 == exchange_num(num_3, 3):
                                result = exchange_num(num_2, 2)
                                break
                            num_3[l] = tmp_3
                num_2[j] = tmp_2


    print('#{} {}'.format(tc, result))
