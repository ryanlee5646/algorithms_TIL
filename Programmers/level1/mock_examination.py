# Level1 모의고사

# 비교배열 개수
def arr_count(answers, type):
    if len(answers) > len(type):
        return type * (len(answers)//len(type) + 1)
    return type
# 정답수
def answer_count(answers, type):
    count = 0
    for i in range(len(answers)):
        if answers[i] == type[i]:
            count += 1
    return count

def solution(answers):
    type_1 = arr_count(answers, [1, 2, 3, 4, 5])
    type_2 = arr_count(answers, [2, 1, 2, 3, 2, 4, 2, 5])
    type_3 = arr_count(answers, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    t1_count = answer_count(answers, type_1)
    t2_count = answer_count(answers, type_2)
    t3_count = answer_count(answers, type_3)
    
    dict_result = {1 : t1_count, 2 : t2_count, 3 : t3_count}
    # 등수구하기
    answer = [t for t, count in dict_result.items() if count == max(dict_result.values())]
    
    return answer