# 균형잡힌 문자열 체크
def is_balance(p):
    left, right = 0
    for i in p:
        if i == '(':
            left += 1
        else: 
            right += 1
    if left == right:
        return True
    return False

# 올바른 문자 체크
def divide(p):
    stack = []
    
    for i in range(len(p)):
        if len(stack) == 0:
            stack.append(p[i])
            if stack[-1] == ')':
                return False
        elif p[i] == '(':
            stack.append(p[i])
        else: 
            stack.pop()
        print(stack)
    return True

def solution(p):
    #1. 빈 문자열인 경우 반환
    if p == '':
        return p
    #1-1 전체가 올바른 문자열일 경우 리턴
    if is_correct(p):
        print(True)
        return p
    else:
        print(False)
    
    return 


solution("(()))()())")