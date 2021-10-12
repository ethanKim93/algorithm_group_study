T = int(input())

table = {
    '0' : ['1', '2'],
    '1' : ['0', '2'],
    '2' : ['0', '1'],
}

def transform_tenary(num_list, number, pos):
    temp = number[pos]
    for num in table[number[pos]]:
        number[pos] = num
        num_list.append(int("".join(number[:]), 3))
        number[pos] = temp

def check(bin_list, ten_list):
    for bin_num in bin_list:
        for ten_num in ten_list:
            if bin_num == ten_num:
                return bin_num

for tc in range(1, T + 1):
    binary = input()
    num_bin = len(binary)
    tenary = input()
    num_ten = len(tenary)

    bin_list = []
    ten_list = []
    
    binary = int(binary, 2)
    tenary = list(tenary)

    for i in range(num_bin):
        bin_list.append(binary ^ (1 << i))
    
    for i in range(num_ten):
        transform_tenary(ten_list, tenary, i)
    
    print("#{} {}".format(tc, check(bin_list, ten_list)))

