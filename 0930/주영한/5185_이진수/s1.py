def to_binary(hex_num):
    if hex_num.isdigit():
        hex_num = int(hex_num)
    else:
        hex_num = ord(hex_num) - ord('A') + 10
    cnt = 0
    result = ""
    while cnt < 4:
        result = str(hex_num % 2) + result
        hex_num = hex_num // 2
        cnt += 1
    return result

for tc in range(1, int(input()) + 1):
    dummy, texts = input().split()
    result = ""
    for text in texts:
        result = result + to_binary(text)
    print("#{} {}".format(tc, result))