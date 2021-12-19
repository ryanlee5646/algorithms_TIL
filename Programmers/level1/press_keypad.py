# Level1 키패드 누르기

def distance_count(index, number_index):
    result = abs(index[0] - number_index[0]) + abs(index[1] - number_index[1])
    return result

def solution(numbers, hand): 
    left_num = {1:[0,0], 4:[1,0], 7:[2,0]}
    right_num = {3:[0,2], 6:[1,2], 9:[2,2]}
    middle_num = {2:[0,1], 5:[1,1], 8:[2,1], 0:[3,1]}
    answer = ''
    left_index = [3,0]
    right_index = [3,2]
    
    for number in numbers:
        if number in left_num:
            answer += 'L'
            left_index = left_num[number]
        elif number in right_num:
            answer += 'R'
            right_index = right_num[number]
            
        else:
            left = distance_count(left_index, middle_num[number])
            right = distance_count(right_index, middle_num[number])
            
            if left < right:
                answer += 'L'
                left_index = middle_num[number]
            elif right < left:
                answer += 'R'
                right_index = middle_num[number]
            else:
                if hand == "left":
                    answer += "L"
                    left_index = middle_num[number]
                else:
                    answer += "R"
                    right_index = middle_num[number]
    return answer