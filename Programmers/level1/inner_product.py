# Level1 내적

# 1
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer
# 2
def solution(a, b):
    answer = 0
    for i,j in zip(a,b):
        answer += a[i] * b[j]
    return answer
# 3
def solution(a, b):
    return sum(i*j for i,j in zip(a,b))