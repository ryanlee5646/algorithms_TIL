# 가변형 인자로 정수들을 입력받아 곱을 반환하는 함수를 정의하고,
# 단, 1, 2, '4', 3와 같이 제대로 입력되지 않은 경우 예외를 처리하는 프로그램을 작성하십시오.

def deci(a):
    result = 1
    for i in a:
        result *= i
    return result
try:
    print(deci(a=list(map(int,input().split(',')))))
except ValueError:
    print("에러발생")        
# a = input().split(',')
# print(a)
# for i in a:
#     if i == int:
#         print(i)        
# a = [1,2,'3',4]
# print(int(a))