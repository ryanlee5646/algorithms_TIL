# 다음과 같이 사용자 2명으로부터 가위, 바위, 보를 입력 받아
# 가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.

user1 = input()
user2 = input()
def rcp(a=input(), b=input()):
    if a == b: return '비김'
    elif a == '바위':
        if b == '가위': return "바위가 이겼습니다!"
        elif b == '보': return "바위가 졌습니다!"
    elif a == '가위':
        if b == '보': return "가위가 이겼습니다!"
        elif b == '바위': return "바위가 이겼습니다!"
    elif a == '보':
        if b == '바위': return "보가 이겼습니다!"
        elif b == '바위': return "보가 졌습니다!"

print(rcp())