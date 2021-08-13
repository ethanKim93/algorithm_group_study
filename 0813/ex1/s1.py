def reverse_str(word):
    # string -> immutable
    my_str = list(word)
    # ['a', 'b', 'c', 'd', 'e']

    """
    자기 문자열을 활용하기 때문에 swap을 위한 임시 변수를 활용한다.
    """
    # 절반 반복을 돌며
    for i in range(len(my_str)//2):
        # i번째 문자를 임시 변수에 옮기고
        tmp = my_str[i]
        # 끝에서부터 문자를 i번째에 옮기고
        my_str[i] = my_str[len(my_str)-1-i]
        # 임시 변수에 옮겼던 i번째 문자를 다시 끝으로 옮기자
        my_str[len(word)-1-i] = tmp

    # ['e', 'd', 'c', 'b', 'a']
    reversed_word = ''.join(my_str)
    return reversed_word


# 방법1. 일반적인 방법
word = 'abcde'
result = reverse_str(word)
print(result)

# 방법2. pythonic
word2 = "Reverse this strings"
word2 = word2[-1:0:-1]
print(word2)