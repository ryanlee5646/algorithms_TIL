# 124 -> '124'

Data = 1244325
result = ''

while Data  > 0:
    result = chr((Data%10)+ord('0')) + result #맨끝에 값을 아스키코드값을 기준으로 더해줌
    Data = Data//10
print(result)
