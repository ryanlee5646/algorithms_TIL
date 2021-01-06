# 다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,
# 60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.

scores = [88, 30, 61, 55, 95]
for num, score  in enumerate(scores):
    if score >= 60:
        print(f'{num+1}번 학생은 {score}점으로 합격입니다.')
    else:
        print(f'{num+1}번 학생은 {score}점으로 불합격입니다.')

