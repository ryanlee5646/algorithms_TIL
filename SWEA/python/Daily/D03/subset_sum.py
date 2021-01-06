import sys
sys.stdin = open("subset_input.txt","r")

arr = [-3, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr) # 원소의 개수

answer = []  # 부분집합 요소
temp = [] # 부분집합을 넣고 합을 구하고 초기화

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            temp.append(arr[j])

    if(sum(temp)==0):
        answer.append(temp)
    temp = []

print(answer)