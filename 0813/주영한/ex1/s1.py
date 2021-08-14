def pythonicstrreverse(text):
    return text[::-1]

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

text = "Reverse this strings"
print(strreverse(text))
print(pythonicstrreverse(text))