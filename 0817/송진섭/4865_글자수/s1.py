import sys
sys.stdin = open('sample_input.txt')


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[min_i] > arr[j]:
                min_i = j
            arr[min_i], arr[i] = arr[i], arr[min_i]
    return arr


def word_count(str1, str2):
    cnt_list = []

    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt +=1
        cnt_list.append(cnt)
    return selection_sort(cnt_list)[-1]

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    print(word_count(str1, str2))