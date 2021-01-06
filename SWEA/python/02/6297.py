# 콤마(,)로 구분해 숫자를 입력하고, 입력된 숫자 중 홀수를 콤마(,)로 구분해 출력하는
# 리스트 내포 기능을 이용한 프로그램을 작성하십시오.

num = list(map(int, input().split(', ')))
num1 = []
for i in num:
    if i % 2:
        num1.append(i)
print(', '.join(map(str,num1)))
