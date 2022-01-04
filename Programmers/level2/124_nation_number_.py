# Level1 124 나라의 숫자

def solution(n):
    answer = ''
    sample = ['1','2','4']
    
    while n:
        if n%3 == 0:
            answer = "4" + answer
            # 나머지가 0인 경우에는 바로 문자열을 붙여주고 몫에서 1을 빼줌(3만큼의 숫자)
            n = n//3 - 1
        else:
            # 나머지는 1 or 2이므로 index 접근을 위해 -1해서 answer 앞쪽에 붙여줌
            answer = sample[n%3-1] + answer
            n = n//3
    return answer
