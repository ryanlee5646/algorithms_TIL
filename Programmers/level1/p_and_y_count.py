# 문자열 내 p와 y의 개수

# 방법 1
def solution(s):
    answer = True
    p_count = 0
    y_count = 0
    for i in s:
        if i == 'p' or i == 'P':
            p_count += 1
        elif i == 'y' or i == 'Y':
            y_count += 1
    if p_count == y_count:
        return True
    else:
        return False
    return True

# 방법 2
def solution(s):
    return s.lower().count('p') == s.lower().count('y')