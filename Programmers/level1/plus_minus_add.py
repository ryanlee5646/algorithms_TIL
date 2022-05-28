# leve1 음양 더하기


def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i] == False:
            print(i)
            answer -= absolutes[i]
        else:
            answer += absolutes[i]

    return answer


result = solution([4, 7, 12], [True, False, True])
print(result)
