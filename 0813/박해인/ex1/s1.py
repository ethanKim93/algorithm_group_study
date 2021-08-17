def reverse_string(words):
    reversed_string = []
    for i in range(len(words)):
        reversed_string.append(words[len(words)-1-i])

    return "".join(reversed_string)

print(reverse_string('ssafy'))

## pythonic
# words[::-1]