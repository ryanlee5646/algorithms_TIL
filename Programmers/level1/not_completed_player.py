# Level1 완주하지 못한 선수

def solution(participant, completion):
    # 1. 리스트 정렬
    participant.sort()
    completion.sort()

    # 2. 완주자 체크
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]

    # 3. for문 다돌아도 없으면 마지막이 완주하지 못한놈
    return participant[-1]