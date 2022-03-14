# 신고 결과 받기

# Test Case 1
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    
    answer = [0] * len(id_list)
    # 중복 신고횟수 제거
    report = set(report)

    # 신고 리스트 초기화
    report_list = {}
    for i in id_list:
        report_list[i] = []
        
    # 유저별 피신고 횟수 카운트를 위한 DIC 생성
    receiver_count = {}
    
    for i in report:
        user,  receiver = i.split(" ")
        # 유저가 누굴 신고했는지 리스트 추가
        report_list[user].append(receiver)
        # 유저별 피신고 횟수 체크
        if receiver not in receiver_count:
            receiver_count[receiver] = 1
        else:
            receiver_count[receiver] += 1
    # k번 이상 피신고 유저 체크 후  
    for receiver in receiver_count:
        if receiver_count[receiver] >= k:
            # 해당 피신고자가 신고자 목록에 있는지 체크
            for i in range(len(id_list)):
                if receiver in report_list[id_list[i]]:
                    answer[i] += 1 
    return answer

result = solution(id_list, report, k)

