import sys
sys.stdin = open("input.txt")

codes = {
    "0001101" : 0,
    "0011001" : 1,
    "0010011" : 2,
    "0111101" : 3,
    "0100011" : 4,
    "0110001" : 5,
    "0101111" : 6,
    "0111011" : 7,
    "0110111" : 8,
    "0001011" : 9
}

def decode_password():
    for password in passwords:
        if '1' in password:
            decode_set = []
            idx = len(password) - 1
            while idx > 0:
                if password[idx] == '1' and codes.get(password[idx - 6 : idx + 1]) != None:
                    decode_set = [codes[password[idx - 6 : idx + 1]]] + decode_set
                    idx -= 7
                    continue
                idx -= 1

            odd_set = 0
            even_set = 0
            certification = 0
            for idx, num in enumerate(decode_set):
                if idx == len(decode_set) - 1:
                    certification = num
                    break
                if idx % 2:
                    even_set += num
                else :
                    odd_set += num

            result = 3 * odd_set + even_set + certification
            if not result % 10:
                return odd_set + even_set + certification
    return 0


T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())
    passwords = [input() for _ in range(R)]
    print("#{} {}".format(tc, decode_password()))