import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t + 1):
    text = list(input())
    flag = True
    while flag:
        new_text = []
        for i in range(len(text)-1):
            if text[i] == text[i+1]:
                for x in text[i+2:]:
                    new_text.append(x)
                break
            else:
                new_text.append(text[i])
                if i == len(text)-2:
                    new_text.append(text[i+1])
        else:
            flag = False

        if flag:
            text = new_text

    print("#{} {}".format(tc,len(text)))