N = int(input())  # 마이쮸 몇번까지 할래?
lst = []  # 줄서는 리스트
idx = [0] * (N+1)  # 대충 순서 넣기
num = [0] * (N+1)  # 인덱스별 마이쮸 개수

# 처음엔 1이 줄을 선다
lst.append(1)

while True:
    i = lst.pop(0)  # 맨앞에 선사람 뽑고
    idx[i] += 1  # 줄선 횟수 +1
    num[i] += idx[i]  # 줄 몇번 섰는지
    if sum(num) >= N:
        print('{}'.format(i))
        break
    lst.append(i)
    lst.append(i+2)
