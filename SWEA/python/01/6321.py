# 소수를 검사하는 함수를 정의하고, 다음의 결과와 같이 사용자가 입력한 숫자가
# 소수인지를 판단하는 프로그램을 작성하십시오.
# 소수일 경우 "소수입니다." 출력, 아닐 경우 "소수가 아닙니다." 출력

def sosoo(num = int(input())):
    count = 0
    if num < 2:
        return '소수가 아닙니다.'
    elif num == 2:
        return '소수입니다.'
    else:
        for i in range(2, num):
            if num % i != 0:
                count+=1
            else:
                return '소수가 아닙니다.'
        return '소수 입니다.'

print(sosoo())
