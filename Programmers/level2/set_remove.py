# leveL2 짝지어 제거하기 

def solution(s):
    tmp = []
    if len(s) % 2 == 1:
        return 0
    for i in s:
        # 비교할 문자열 없으면 넣기
        if len(tmp) == 0: 
            tmp.append(i)
        # 문자열 비교
        elif tmp[-1] == i: 
            tmp.pop()
        # 비교 문자열 추가
        else: 
            tmp.append(i)
    # tmp 배열에 하나도 없으면 1 남아있으면 0 리턴        
    if len(tmp) == 0: 
        return 1
    else: 
        return 0
    
    