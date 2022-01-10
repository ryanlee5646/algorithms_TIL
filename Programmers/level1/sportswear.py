#leve1 체육복

def solution(n, lost, reserve): 
    # 여벌의 옷있는 애가 도난 당했을 때 중복 제거 (그냥 양쪽 다 포함 안되는 놈)
    _reserve = [i for i in reserve if i not in lost]
    _lost = [i for i in lost if i not in reserve]
    
    # 순서가 달라짐에 따라 못받는 애가 생길수도 있으니 차례대로 
    _reserve.sort()
    _lost.sort()
    
    for i in _reserve:
        left = i-1
        right = i+1
        
        if left in _lost:
            _lost.remove(left)
        elif right in _lost:
            _lost.remove(right)
    
    return n-len(_lost) # 전체 학생수에서 체육복 없는애 빼면 참여가능한 하갯ㅇ수