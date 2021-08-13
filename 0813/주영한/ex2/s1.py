#이전에 사용한 reverse 함수 재사용
def strreverse(texts):
    temp_list = []
    # temp_list = list(texts)
    for text in texts:
        temp_list.append(text)

    # reverse algorithm
    for idx in range(len(temp_list) // 2):
        temp = temp_list[idx]
        temp_list[idx] = temp_list[len(temp_list) - 1 - idx]
        temp_list[len(temp_list) - 1 - idx] = temp
    return "".join(temp_list)

def itoa(integer):
    # 음수인지를 판별하고, 양수로 통일한다.
    negative = False
    if integer < 0:
        negative = True
        integer = -integer

    result = []
    while True:
        # 각 자리수에 대해 문자열로 리스트에 추가한다.
        # 문자열로 변환된 값들을 추가한다.
        result.append(chr(integer % 10 + ord("0")))
        if not integer // 10:
            break
        integer = integer // 10

    # 음수일 경우, "-"를 추가한다.
    if negative :
        result.append("-")

    # 문자를 뒤집는다.
    temp_list = strreverse(result)
    return "".join(temp_list)

def stoi(string):

    # 음수인지를 판별하고, 시작하는 인덱스를 조절한다.
    negative = False
    if string[0] == "-":
        negative = True
        string = string[1:]
    result = 0

    for idx in range(len(string)):
        # 각 자리수를 고려하여 문자열을 정수형 타입으로 변환하여 처리한다.
        result += (ord(string[idx]) - ord("0")) * (10 ** (len(string) - 1 - idx))

    # 음수일 경우, "-"를 추가한다.
    if negative :
        result *= -1

    return result

print("itoa example")
a = itoa(10000)
print(a, type(a))
b = itoa(-10000)
print(b, type(b))
c = itoa(0)
print(c, type(c))
d = itoa(3521)
print(d, type(d))
e = itoa(-3521)
print(e, type(e))
print()

print("stoi example")
a = stoi("10000")
print(a, type(a))
b = stoi("-10000")
print(b, type(b))
c = stoi("0")
print(c, type(c))
d = stoi("3521")
print(d, type(d))
e = stoi("-3521")
print(e, type(e))