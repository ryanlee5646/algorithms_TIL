# Level1 없는숫자 더하기

# def solution(numbers):
#     sample = [0,1,2,3,4,5,6,7,8,9]
#     answer = 0
#     for number in numbers:
#         sample.remove(number)
#     answer = sum(sample)
#     return answer

def solution(numbers):
    return sum(range(10)) - sum(numbers)