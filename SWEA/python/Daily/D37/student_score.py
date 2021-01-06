import sys
sys.stdin = open("student_score.txt","r")

T = int(input())
score = ['A+','A0','A-','B+','B0', 'B-', 'C+', 'C0', 'C-','D0']
for t in range(1,T+1):
    N, K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]

    total_score = {}
    for i in range(0,N):
        temp = (data[i][0]*0.35) + (data[i][1]*0.45) + (data[i][2]*0.2)
        total_score[i] = temp
    result = sorted(total_score.values(), reverse=True) # value 값이 내림차순정렬되있음

    grade = result.index(total_score[K-1]) # 내림차순 정렬되 있는 result에서 몇번째 학생이
    # 저장되 있는지 알려주는 dictionary형태의 total_score에서 키값으로 점수를 알아낸다

    print("#{} {}".format(t,score[int((grade/int(N))*10)]))
