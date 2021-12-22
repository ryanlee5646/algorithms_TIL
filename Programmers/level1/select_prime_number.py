# 소수 찾기

def prime_number(num):
    arr = [True] * (num+1)
    for i in range(2, num+1):
        if arr[i] == True:           # i가 소수인 경우
            for j in range(i*2, num+1, i): # 소수의 배수 제거
                arr[j] = False
    return arr


def solution(n):
    answer = 0
    result_arr = prime_number(n)
    for i in range(2, n+1): # 첫번째 소수부터 카운트
        if result_arr[i] == True:
            answer+=1
    return answer