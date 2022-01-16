# 윤년

# 윤년구하기 함수
def leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return 1
    return 0

t = int(input())

print(leap_year(t))
