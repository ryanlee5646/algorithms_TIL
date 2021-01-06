# 다음과 같이 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한
# 팩토리얼 값을 구하는 프로그램을 작성하십시오.

# def facto():
#     num = int(input())
#     facto = 1
#     if num < 2:
#         return num
#     else:
#         for i in range(1,num+1):
#             facto = (facto*i)
#     return facto
# print(facto())


# 재귀
def facto(num = int(input())):
    if num < 2:
        return num
    else:
        return num * facto(num-1)
print(facto(5))