# 다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아
# 이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.
# 입력: 2, 3, 4, 5    출력: 12.57, 18.85, 25.13, 31.42
import math
r = map(int, input().split(','))
circle = []
for i in r:
    result = (i+i)*math.pi
    circle.append(round(result,2))
print(', '.join(map(str, circle)))
