# 다음의 결과와 같이 이름과 나이를 입력 받아
# 올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오
# 입력                         출력
# 홍길동                  홍길동(은)는 2098년에 100세가 될 것입니다.
# 20

from datetime import datetime

this_year = datetime.today().year
name = input()
age = int(input())
remain_age = 100 - age
future_year = this_year + remain_age
print(f'{name}(은)는 {future_year}년에 100세가 될 것입니다. ')

# name = input()
# age = int(input())
# future = 100 - age
# future_year = 2019 + future
# print(f'{name}(은)는 {future_year}년에 100세가 될 것입니다. ')