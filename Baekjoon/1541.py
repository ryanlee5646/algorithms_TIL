# 잃어버린 괄호

def bracket(t):
    #2 배열의 첫번째으로 초기화 해줌(음수는 존재하지 않으므로 처음에는 무조건 더해줌)
    answer = sum(list(map(int,t[0].split('+'))))
    
    #3 배열의 두번째 값부터 +연산자 기준으로 더함
    for i in t[1:]:
        tmp = i.split('+')
        count = 0
        for j in tmp:
            count += int(j)
    #4 괄호안에 값을 더한 후 빼줌
        answer -= count
    return answer

#1. 마이너스 기준으로 입력 값을 받음
# "55-50+40" -> [55, 50+40]
t = input().split('-')

print(bracket(t))