# 정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,
# 이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.
# [2, 4, 6, 8, 10]
# 5 => False
# 10 => True
a = [2, 4, 6, 8, 10]
b = [5, 10]
def find(a, b):
    for i in b:
        if i in b:
            return f'{b} => False'
        else:
            return f'{b} => True'
for j in b:
    print(find(a, b))

